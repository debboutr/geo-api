# encoding: utf-8

from app import api_v1


class NRSA1314ApiNamespace:
    namespace = "nrsa1314"
    description = (
        "data collected from survey sites in the National Aquatic "
        "Resource Survey 2013-14\n "
        "https://www.epa.gov/national-aquatic-resource-surveys/"
        "national-rivers-and-streams-assessment-2013-2014-results"
    )


def init_app(app, **kwargs):
    """
    Init the GeoAPI module.
    """

    # Load the underlying module
    from . import resources

    api_v1.add_namespace(resources.api)
