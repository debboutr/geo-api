from flask_restx import Namespace, fields


ns = Namespace("models")


point = ns.model(
    "Point Geometry",
    {
        "type": fields.String(read_only=True),
        "coordinates": fields.List(
            fields.Float,
            required=True,
            type="array",
            example=[-108.4182, 36.75052],
        ),
    },
    mask={"type"},
)


list_props = ns.model(
    "List Feature Properties",
    {
        "SITE_ID": fields.String(required=True, description="Site Identification Code"),
        "DATE_COL": fields.String(required=True, description="Date of Site Visit"),
        "YEAR": fields.String(required=True, description="Year of Site Visit"),
        "VISIT_NO": fields.String(
            required=True, description="Within Year Site Visit Number"
        ),
    },
)

detail_props_0809 = ns.inherit(
    "0809 Detail Feature Properties",
    list_props,
    {
        "MAJ_BAS_NM": fields.String(
            required=True,
            description="Major USGS Hydrologic Basins derived from NHDPlus",
        ),
        "XCOORD": fields.String(
            required=True,
            description="x-coordinate from US Contiguous Albers Equal Area Conic projection",
        ),
        "YCOORD": fields.String(
            required=True,
            description="y-coordinate from US Contiguous Albers Equal Area Conic projection",
        ),
        "AG_ECO3_NM": fields.String(
            required=True, description="NARS 3-level reporting region Name"
        ),
        "AG_ECO9_NM": fields.String(
            required=True, description="NARS 9-level reporting region Name"
        ),
        "MISS_BASIN_NM": fields.String(
            required=True, description="Mississippi basin name"
        ),
        "FS_EW": fields.String(
            required=True, description="Eastern or western US Forest Service land"
        ),
        "EPA_REG": fields.String(required=True, description="EPA Region"),
        "STRAH_CAT": fields.String(
            required=True, description="Strahler category used to classify reaches"
        ),
        "NARS_OWN": fields.String(
            required=True, description="Land ownership category used by NARS"
        ),
        "NRS13_EVAL": fields.String(
            required=True, description="NRSA 2013/14 site evaluation result"
        ),
        "NRS13_MDC": fields.String(
            required=True,
            description="Multi-density categories used in NRSA 2013/14 survey design within a stratum",
        ),
        "NRS13_PNL": fields.String(
            required=True, description="NRSA 2013/14 Panel Assignment"
        ),
        "NRS13_SF": fields.String(
            required=True,
            description="Lake included/excluded from NRSA 2013/14 survey design",
        ),
        "NRS13_STRA": fields.String(
            required=True, description="Strata used in NRSA 2013/14 survey design"
        ),
        "NRS13_TNT": fields.String(
            required=True,
            description="NRS 2013/14 target status assigned based on stream site evaluation for use in national assessments",
        ),
        "NRS13_URBN": fields.String(
            required=True,
            description="Stream site identified as an urban or non-urban stream. Source: https://www.census.gov/geo/maps-data/data/cbf/cbf_ua.html",
        ),
        "NRS13_VST": fields.String(
            required=True,
            description="Number of times NRSA 2013/14 site was actually sampled in 2013/14",
        ),
        "WGT_EXT_SP": fields.String(
            required=True,
            description="Length of sampled streams represented by site in km",
        ),
        "PUBLICATION_DATE": fields.String(
            required=True, description="Date of data file publication"
        ),
        "ANC_COND": fields.String(
            required=True, description="Site condition class based on acidity"
        ),
        "ANC": fields.String(
            required=True, description="Acid Neutralizing Capacity - MG N/L"
        ),
        "DOC": fields.String(
            required=True, description="Dissolved Organic Carbon - MG/L"
        ),
        "PH": fields.String(required=True, description="pH - STD. UNITS"),
        "SAL_COND": fields.String(
            required=True,
            description="Site condition class based on conductivity	Good|Fair|Poor|No Data",
        ),
        "COND": fields.String(
            required=True, description="Conductivity - US/CM AT 25 C"
        ),
        "NTL_COND": fields.String(
            required=True,
            description="Site condition class based on total nitrogen concentration	Good|Fair|Poor|No Data",
        ),
        "NTL_UG_L": fields.String(required=True, description="Total Nitrogen - UG N/L"),
        "PTL_COND": fields.String(
            required=True,
            description="Site condition class based on total phosphorus concentration	Good|Fair|Poor|No Data",
        ),
        "PTL": fields.String(required=True, description="Total Phosphorus - UG/L"),
        "BENT_MMI_COND": fields.String(
            required=True,
            description="Condition class based on benthic MMI score	Good|Fair|Poor|Not Assessed",
        ),
        "MMI_BENT": fields.String(
            required=True,
            description="Benthic MMI score	Good|Fair|Poor|Not Assessed	0	100",
        ),
        "OE_SCORE": fields.String(
            required=True, description="O/E score for benthic sample"
        ),
        "OE_COND": fields.String(
            required=True,
            description="Condition class based on O/E score	<0.5|<0.8|<0.9|>=0.9",
        ),
        "INSTRMCVR_COND": fields.String(
            required=True,
            description="Instream cover condition, based in log natural fish cover (L_XFC_NAT)	Good|Fair|Poor|Not Assessed",
        ),
        "L_XFC_NAT": fields.String(required=True, description="Log10(XFC_NAT + 0.01)"),
        "BEDSED_COND": fields.String(
            required=True,
            description="Bed sediment condition, based on log relative bed stability (LRBS_use)",
        ),
        "LRBS_USE": fields.String(
            required=True,
            description="Log relative bed stability to use in assessing BEDSED_COND, filled in from other variables as needed",
        ),
        "RIPDIST_COND": fields.String(
            required=True,
            description="Riparian disturbance condition, based on W1_HALL",
        ),
        "W1_HALL": fields.String(
            required=True,
            description="Human Disturbance Index(distance-wtd tally of types and presence used for condition",
        ),
        "RIPVEG_COND": fields.String(
            required=True, description="Riparian vegetation condition, based on L_XCMGW"
        ),
        "L_XCMGW": fields.String(required=True, description="Log10(XCMGW + 0.01)"),
        "FISH_MMI_COND": fields.String(
            required=True,
            description="Fish assemblage condition, based on regional Fish MMI.",
        ),
        "MMI_FISH": fields.String(
            required=True,
            description="Traditional MMI watershed adjusted value for MMI_FISH",
        ),
        "ENT_1X_CCE_100ML": fields.String(
            required=True,
            description="Estimated enterococci CCE / 100 mL of water sample volume from ORD analysis of undiluted DNA extracts and  CCE / extract calculations from EPA Method 1609 calculation spreadsheet.  CCE are based on 15:1 calibrator target sequence equivalent (CSE) to CCE ratio established for RWQC guideline values. CCE /  extract was multiplied by 100 ÷ filtered sample volume to obtain final estimate /100 ml",
        ),
        "ENT_1X_STV_COND": fields.String(
            required=True,
            description="Estimated enterococci CCE / 100 mL of water sample volume from ORD analyses of undiluted DNA extract and calculations from EPA Method 1609 calculation spreadsheet exceeds (1) or is less than (0) RWQC STV value of 1280 CCE/100 mL",
        ),
        "MICX_COND": fields.String(
            required=True,
            description="Microcystin condition class	<= 8 ug/L|> 8 ug/L|Not Detected",
        ),
        "MICX_RESULT": fields.String(
            required=True, description="Result for Microcystin - UG/L"
        ),
        "MICX_MDL": fields.String(
            required=True, description="Minimum Detection Limit for Microcystin - UG/L"
        ),
        "MICX_RL": fields.String(
            required=True, description="Reporting Limit for Microcystin - UG/L"
        ),
        "MICX_FLAG": fields.String(
            required=True, description="NARS flag for analyte Microcystin"
        ),
        "HG_COND": fields.String(
            required=True,
            description="Site condition class based on mercury concentration in fish tissue	Does Not Exceed 300 mg Hg/g ww|Exceeds 300 mg Hg/g ww|No Data|Not Assessed|No Sample Collected",
        ),
        "MERCURY_RESULT": fields.String(
            required=True, description="Result for Mercury in Fish Tissue - NG/G"
        ),
        "MERCURY_MDL": fields.String(
            required=True,
            description="Minimum Detection Limit for Mercury in Fish Tissue - NG/G",
        ),
        "MERCURY_RL": fields.String(
            required=True,
            description="Reporting Limit for Mercury in Fish Tissue - NG/G",
        ),
        "MERCURY_FLAG": fields.String(
            required=True, description="NARS flag for analyte Mercury"
        ),
        "MERCURY_DATA_FLAG": fields.String(
            required=True, description="Laboratory or OW flag of result for Mercury"
        ),
        "MERCURY_COMMENT": fields.String(
            required=True,
            description="Comment to indicate reason mercury data not used in assessment",
        ),
    },
)

detail_props_1314 = ns.inherit(
    "1314 Detail Feature Properties",
    list_props,
    {
        "MAJ_BAS_NM": fields.String(
            required=True,
            description="Major USGS Hydrologic Basins derived from NHDPlus",
        ),
        "XCOORD": fields.String(
            required=True,
            description="x-coordinate from US Contiguous Albers Equal Area Conic projection",
        ),
        "YCOORD": fields.String(
            required=True,
            description="y-coordinate from US Contiguous Albers Equal Area Conic projection",
        ),
        "AG_ECO3_NM": fields.String(
            required=True, description="NARS 3-level reporting region Name"
        ),
        "AG_ECO9_NM": fields.String(
            required=True, description="NARS 9-level reporting region Name"
        ),
        "MISS_BASIN_NM": fields.String(
            required=True, description="Mississippi basin name"
        ),
        "FS_EW": fields.String(
            required=True, description="Eastern or western US Forest Service land"
        ),
        "EPA_REG": fields.String(required=True, description="EPA Region"),
        "STRAH_CAT": fields.String(
            required=True, description="Strahler category used to classify reaches"
        ),
        "NARS_OWN": fields.String(
            required=True, description="Land ownership category used by NARS"
        ),
        "NRS13_EVAL": fields.String(
            required=True, description="NRSA 2013/14 site evaluation result"
        ),
        "NRS13_MDC": fields.String(
            required=True,
            description="Multi-density categories used in NRSA 2013/14 survey design within a stratum",
        ),
        "NRS13_PNL": fields.String(
            required=True, description="NRSA 2013/14 Panel Assignment"
        ),
        "NRS13_SF": fields.String(
            required=True,
            description="Lake included/excluded from NRSA 2013/14 survey design",
        ),
        "NRS13_STRA": fields.String(
            required=True, description="Strata used in NRSA 2013/14 survey design"
        ),
        "NRS13_TNT": fields.String(
            required=True,
            description="NRS 2013/14 target status assigned based on stream site evaluation for use in national assessments",
        ),
        "NRS13_URBN": fields.String(
            required=True,
            description="Stream site identified as an urban or non-urban stream. Source: https://www.census.gov/geo/maps-data/data/cbf/cbf_ua.html",
        ),
        "NRS13_VST": fields.String(
            required=True,
            description="Number of times NRSA 2013/14 site was actually sampled in 2013/14",
        ),
        "WGT_EXT_SP": fields.String(
            required=True,
            description="Length of sampled streams represented by site in km",
        ),
        "PUBLICATION_DATE": fields.String(
            required=True, description="Date of data file publication"
        ),
        "ANC_COND": fields.String(
            required=True, description="Site condition class based on acidity"
        ),
        "ANC": fields.String(
            required=True, description="Acid Neutralizing Capacity - MG N/L"
        ),
        "DOC": fields.String(
            required=True, description="Dissolved Organic Carbon - MG/L"
        ),
        "PH": fields.String(required=True, description="pH - STD. UNITS"),
        "SAL_COND": fields.String(
            required=True,
            description="Site condition class based on conductivity	Good|Fair|Poor|No Data",
        ),
        "COND": fields.String(
            required=True, description="Conductivity - US/CM AT 25 C"
        ),
        "NTL_COND": fields.String(
            required=True,
            description="Site condition class based on total nitrogen concentration	Good|Fair|Poor|No Data",
        ),
        "NTL_UG_L": fields.String(required=True, description="Total Nitrogen - UG N/L"),
        "PTL_COND": fields.String(
            required=True,
            description="Site condition class based on total phosphorus concentration	Good|Fair|Poor|No Data",
        ),
        "PTL": fields.String(required=True, description="Total Phosphorus - UG/L"),
        "BENT_MMI_COND": fields.String(
            required=True,
            description="Condition class based on benthic MMI score	Good|Fair|Poor|Not Assessed",
        ),
        "MMI_BENT": fields.String(
            required=True,
            description="Benthic MMI score	Good|Fair|Poor|Not Assessed	0	100",
        ),
        "OE_SCORE": fields.String(
            required=True, description="O/E score for benthic sample"
        ),
        "OE_COND": fields.String(
            required=True,
            description="Condition class based on O/E score	<0.5|<0.8|<0.9|>=0.9",
        ),
        "INSTRMCVR_COND": fields.String(
            required=True,
            description="Instream cover condition, based in log natural fish cover (L_XFC_NAT)	Good|Fair|Poor|Not Assessed",
        ),
        "L_XFC_NAT": fields.String(required=True, description="Log10(XFC_NAT + 0.01)"),
        "BEDSED_COND": fields.String(
            required=True,
            description="Bed sediment condition, based on log relative bed stability (LRBS_use)",
        ),
        "LRBS_USE": fields.String(
            required=True,
            description="Log relative bed stability to use in assessing BEDSED_COND, filled in from other variables as needed",
        ),
        "RIPDIST_COND": fields.String(
            required=True,
            description="Riparian disturbance condition, based on W1_HALL",
        ),
        "W1_HALL": fields.String(
            required=True,
            description="Human Disturbance Index(distance-wtd tally of types and presence used for condition",
        ),
        "RIPVEG_COND": fields.String(
            required=True, description="Riparian vegetation condition, based on L_XCMGW"
        ),
        "L_XCMGW": fields.String(required=True, description="Log10(XCMGW + 0.01)"),
        "FISH_MMI_COND": fields.String(
            required=True,
            description="Fish assemblage condition, based on regional Fish MMI.",
        ),
        "MMI_FISH": fields.String(
            required=True,
            description="Traditional MMI watershed adjusted value for MMI_FISH",
        ),
        "ENT_1X_CCE_100ML": fields.String(
            required=True,
            description="Estimated enterococci CCE / 100 mL of water sample volume from ORD analysis of undiluted DNA extracts and  CCE / extract calculations from EPA Method 1609 calculation spreadsheet.  CCE are based on 15:1 calibrator target sequence equivalent (CSE) to CCE ratio established for RWQC guideline values. CCE /  extract was multiplied by 100 ÷ filtered sample volume to obtain final estimate /100 ml",
        ),
        "ENT_1X_STV_COND": fields.String(
            required=True,
            description="Estimated enterococci CCE / 100 mL of water sample volume from ORD analyses of undiluted DNA extract and calculations from EPA Method 1609 calculation spreadsheet exceeds (1) or is less than (0) RWQC STV value of 1280 CCE/100 mL",
        ),
        "MICX_COND": fields.String(
            required=True,
            description="Microcystin condition class	<= 8 ug/L|> 8 ug/L|Not Detected",
        ),
        "MICX_RESULT": fields.String(
            required=True, description="Result for Microcystin - UG/L"
        ),
        "MICX_MDL": fields.String(
            required=True, description="Minimum Detection Limit for Microcystin - UG/L"
        ),
        "MICX_RL": fields.String(
            required=True, description="Reporting Limit for Microcystin - UG/L"
        ),
        "MICX_FLAG": fields.String(
            required=True, description="NARS flag for analyte Microcystin"
        ),
        "HG_COND": fields.String(
            required=True,
            description="Site condition class based on mercury concentration in fish tissue	Does Not Exceed 300 mg Hg/g ww|Exceeds 300 mg Hg/g ww|No Data|Not Assessed|No Sample Collected",
        ),
        "MERCURY_RESULT": fields.String(
            required=True, description="Result for Mercury in Fish Tissue - NG/G"
        ),
        "MERCURY_MDL": fields.String(
            required=True,
            description="Minimum Detection Limit for Mercury in Fish Tissue - NG/G",
        ),
        "MERCURY_RL": fields.String(
            required=True,
            description="Reporting Limit for Mercury in Fish Tissue - NG/G",
        ),
        "MERCURY_FLAG": fields.String(
            required=True, description="NARS flag for analyte Mercury"
        ),
        "MERCURY_DATA_FLAG": fields.String(
            required=True, description="Laboratory or OW flag of result for Mercury"
        ),
        "MERCURY_COMMENT": fields.String(
            required=True,
            description="Comment to indicate reason mercury data not used in assessment",
        ),
    },
)

detail_0809_point_feature = ns.model(
    "0809 Point Feature",
    {
        "type": fields.String(required=True, default="Feature"),
        "geometry": fields.Nested(point, required=True),
        "properties": fields.Nested(detail_props_0809),
    },
)

detail_1314_point_feature = ns.inherit(
    "1314 Point Feature ",
    {
        "type": fields.String(required=True, default="Feature"),
        "geometry": fields.Nested(point, required=True),
        "properties": fields.Nested(detail_props_1314),
    },
)

list_point_feature = ns.model(
    "List Point Feature",
    {
        "type": fields.String(required=True, default="Feature"),
        "properties": fields.Nested(list_props, required=True),
        "geometry": fields.Nested(point, required=True),
    },
)

points_feature = ns.model(
    "Points Feature Collection",
    {
        "type": fields.String(required=True, default="FeatureCollection"),
        "features": fields.List(fields.Nested(list_point_feature, required=True)),
    },
)


polygon = ns.model(
    "Polygon Geometry",
    {
        "type": fields.String(required=True, default="Polygon"),
        "coordinates": fields.List(
            fields.List(fields.Float, required=True, type="Array"),
            required=True,
            type="Array",
            default=[
                [-108.841593, 49.603365],
                [-108.806298, 49.573689],
                [-108.766716, 49.563465],
                [-108.771584, 49.556945],
            ],
        ),
    },
)

polygon_feature = ns.model(
    "Polygon Feature",
    {
        "type": fields.String(default="Feature", require=True),
        "geometry": fields.Nested(polygon, required=True),
    },
)


linestring = ns.model(
    "Line String Geometry",
    {
        "type": fields.String(required=True, default="LineString"),
        "coordinates": fields.List(
            fields.List(fields.Float, required=True, type="Array"),
            required=True,
            type="Array",
            default=[
                [-108.841593, 49.603365],
                [-108.806298, 49.573689],
                [-108.766716, 49.563465],
                [-108.771584, 49.556945],
            ],
        ),
    },
)

linestring_feature = ns.model(
    "Line String Feature",
    {
        "type": fields.String(default="Feature", require=True),
        "geometry": fields.Nested(linestring, required=True),
    },
)