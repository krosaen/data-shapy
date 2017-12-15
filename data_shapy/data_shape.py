def summarize_data_shape(example):
    """
    Given some (json serializeable) example, provide a concise summary of its structure
    by pruning it down to e.g one item per list.
    """

    def is_ground(item):
        return any([
            item is None,
            isinstance(item, bool),
            isinstance(item, int),
            isinstance(item, str),
            isinstance(item, float),
        ])

    def non_none_kv_count(d):
        return len([v for k, v in d.items() if v is not None])

    def max_index(l):
        max_i = 0
        max_v = l[0]
        for i, el in enumerate(l):
            if el > max_v:
                max_i = i
                max_v = el
        return max_i

    if is_ground(example):
        return example

    if isinstance(example, list) or isinstance(example, tuple):
        if len(example) < 10 and all(map(is_ground, example)):
            return example
        elif all([isinstance(el, dict) for el in example[:20]]):
            # we have a list of dicts, find one to summarize that has the most non-null key values
            # (looking 20 items out max)
            non_none_kv_counts = [non_none_kv_count(d) for d in example[:20]]
            return [summarize_data_shape(example[max_index(non_none_kv_counts)])]
        else:
            return [summarize_data_shape(example[0])]

    if isinstance(example, dict):
        return {k: summarize_data_shape(v) for k, v in example.items()}

    raise ValueError("dunno how to deal with type {}".format(type(example)))
