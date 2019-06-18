from com.sun.star.beans import PropertyValue


def uno_props(**kwargs):
    props = []
    for key in kwargs:
        prop = PropertyValue()
        prop.Name = key
        prop.Value = kwargs[key]
        props.append(prop)
    return tuple(props)
