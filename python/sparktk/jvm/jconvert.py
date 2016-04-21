from sparktk.dtypes import dtypes


class JConvert(object):
    """Handles misc. conversions going to and from Scala for simple non-primitive types, like lists, option, etc."""

    def __init__(self, jutils):
        self.jutils = jutils
        self.sc = jutils.sc
        self.scala = self.sc._jvm.org.trustedanalytics.at.jvm.JConvert

    def list_to_double_list(self, python_list):
        return [float(item) for item in python_list]

    def to_scala_list_double(self, python_list):
        return self.scala.toScalaList(self.list_to_double_list(python_list))

    def to_scala_list_string(self, python_list):
        return self.scala.toScalaList([unicode(item) for item in python_list])

    def to_scala_vector_double(self, python_list):
        return self.scala.toScalaVector(self.list_to_double_list(python_list))

    def to_scala_vector_string(self, python_list):
        return self.scala.toScalaVector([unicode(item) for item in python_list])

    def scala_map_string_int_to_python(self, m):
        return dict([(entry[0], int(entry[1])) for entry in list(self.scala.scalaMapStringIntToPython(m))])

    def scala_map_string_seq_to_python(self, m):
        return dict(self.scala.scalaMapStringSeqToPython(m))

    def to_scala_option(self, item):
        return self.scala.toOption(item)

    def to_scala_option_list_double(self, python_list):
        if isinstance(python_list, list):
            python_list = self.list_to_double_list(python_list)
        return self.to_scala_option(python_list)

    def from_scala_option(self, item):
        return self.scala.fromOption(item)
