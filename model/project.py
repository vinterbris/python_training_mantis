from sys import maxsize


class Project:
    def __init__(self, id=None, name=None, status=None, inherit_global=None, view_state=None, description=None,
                 enabled=None):
        self.id = id
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.enabled = enabled

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
