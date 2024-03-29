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
        "COMID": fields.String(required=True, description="COMID of site's catchment"),
        "DATE_COL": fields.String(required=True, description="Date of Site Visit"),
        "YEAR": fields.String(required=True, description="Year of Site Visit"),
        "WSAREASQKM": fields.String(
            required=True, description="Area of the Watershed of the site"
        ),
        "VISIT_NO": fields.String(
            required=True, description="Within Year Site Visit Number"
        ),
    },
)

detail_props_0809 = ns.inherit(
    "0809 Detail Feature Properties",
    list_props,
    {
        "AGGR_ECO3_2015": fields.String(
            required=True,
            description="NARS 3-level reporting region (2015), based on aggregating AGGR_ECO9_2015 reporting regions: EHIGH=Eastern Highlands (NAP, SAP); PLNLOW=Plains and Lowlands (CPL, NPL, SPL, TPL, UMW); WMTNS=Western Mountains and Xeric (WMT, XER).",
        ),
        "AGGR_ECO9_2015": fields.String(
            required=True,
            description="NARS 9-level reporting region (2015), based on aggregated Omernik Level III ecoregions: CPL=Coastal Plains; NAP=Northern Appalachians; NPL=Northern Plains; SAP=Southern Appalachians; SPL=Southern Plains; TPL=Temperate Plains; UMW=Upper Midwest; WMT=Western Mountains; XER=Xeric West.",
        ),
        "DATE_COL": fields.String(
            required=True,
            description="Date of field collection",
        ),
        "EPA_REG": fields.String(
            required=True,
            description="EPA region",
        ),
        "GREAT_RIVER": fields.String(
            required=True,
            description="Great river site",
        ),
        "HUC8": fields.String(
            required=True,
            description="8-digit HUC catalog unit number",
        ),
        "INDEXVIS_FTIS": fields.String(
            required=True,
            description="Index visit for NRSA population estimates for fish tissue only",
        ),
        "INDEX_VISIT": fields.String(
            required=True,
            description="Index visit for NRSA population estimates",
        ),
        "LAT_DD83": fields.String(
            required=True,
            description="Nominal latitude in decimal degrees",
        ),
        "LMR_SITE": fields.String(
            required=True,
            description="Lower Mississippi River site",
        ),
        "LOC_NAME": fields.String(
            required=True,
            description="Site name from verification form",
        ),
        "LON_DD83": fields.String(
            required=True,
            description="Nominal longitude in decimal degrees",
        ),
        "MASTER_SITEID": fields.String(
            required=True,
            description="If used in WSA, WSA Site_ID. If new, current Site_ID",
        ),
        "MISS_SUB": fields.String(
            required=True,
            description="Mississippi sub-basin",
        ),
        "RT_NRSA": fields.String(
            required=True,
            description="Reference/So-so/Trashed designations for sites used in NRSA",
        ),
        "RT_NRSA_CAT": fields.String(
            required=True,
            description="Impact designations for use in indicator development for NRSA",
        ),
        "RT_NRSA_FISH": fields.String(
            required=True,
            description="RT_NRSA designation specific to Fish indicator development",
        ),
        "RT_NRSA_PHAB": fields.String(
            required=True,
            description="RT_NRSA designation specific to physical habitat indicator development, based separate criteria",
        ),
        "SITE_CLASS": fields.String(
            required=True,
            description="Site class (NAWQA, PROB, HAND)",
        ),
        "SITE_ID": fields.String(
            required=True,
            description="Site identification code",
        ),
        "STATE": fields.String(
            required=True,
            description="State in which site located",
        ),
        "STRAHLERORDER": fields.String(
            required=True,
            description="Strahler stream order from RF3 stream data",
        ),
        "UID": fields.String(
            required=True,
            description="Unique site visit ID",
        ),
        "URBAN": fields.String(
            required=True,
            description="Urban site",
        ),
        "US_L3CODE_2015": fields.String(
            required=True,
            description="Omernik Level III ecoregion code (2015)",
        ),
        "US_L4CODE_2015": fields.String(
            required=True,
            description="Omernik Level IV ecoregion code (2015)",
        ),
        "VARIABLE": fields.String(
            required=True,
            description="DESCRIPTION"
            "SAMPLE_TYPE"
            "UNITS"
            "RANGE_LOW"
            "RANGE_HIGH"
            "LEGAL_VALUES",
        ),
        "VISIT_NO": fields.String(
            required=True,
            description="Visit number for that year",
        ),
        "WGTNRSA09": fields.String(
            required=True,
            description="NRSA population weight for site",
        ),
        "XLAT_DD": fields.String(
            required=True,
            description="X-site GPS latitude decimal degrees",
        ),
        "XLON_DD": fields.String(
            required=True,
            description="X-site GPS longitude decimal degrees",
        ),
        "YEAR": fields.String(
            required=True,
            description="Sampling year",
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
            fields.List(
                fields.List(fields.Float, required=True),
                required=True,
                type="Array",
                default=[
                    [-108.841593, 49.603365],
                    [-108.806298, 49.573689],
                    [-108.766716, 49.563465],
                    [-108.771584, 49.556945],
                    [-108.841593, 49.603365],
                ],
            ),
            required=True,
            type="Array",
            default=[],
        ),
    },
)

epa_props = ns.model(
    "EPA Region Properties",
    {
        "EPAREGION": fields.String(
            required=True, description="Site Identification Code"
        ),
    },
)

polygon_feature = ns.model(
    "Polygon Feature",
    {
        "type": fields.String(default="Feature", require=True),
        "properties": fields.Nested(epa_props),
        "geometry": fields.Nested(polygon, required=True),
    },
)

multipolygon = ns.model(
    "MultiPolygon Geometry",
    {
        "type": fields.String(required=True, default="MultiPolygon"),
        "coordinates": fields.List(
            fields.List(
                fields.List(
                    fields.List(fields.Float, required=True),
                    required=True,
                    type="Array",
                    default=[
                        [-108.841593, 49.603365],
                        [-108.806298, 49.573689],
                        [-108.766716, 49.563465],
                        [-108.771584, 49.556945],
                        [-108.841593, 49.603365],
                    ],
                ),
                required=True,
                type="Array",
                default=[],
            ),
            required=True,
            type="Array",
            default=[],
        ),
    },
)

multipolygon_collection = ns.model(
    "MultiPolygon Feature Collection",
    {
        "type": fields.String(default="Feature", require=True),
        "features": fields.Nested(polygon_feature, required=True),
    },
)


detail_props_0405 = ns.inherit(
    "0405 Detail Feature Properties",
    list_props,
    {
        "SITE_ID": fields.String(required=True, description="Site Identification Code"),
        "YEAR": fields.String(required=True, description="Year of Site Visit"),
        "VISIT_NO": fields.String(
            required=True, description="Within Year Site Visit Number"
        ),
        "SITENAME": fields.String(required=True, description="Site Name"),
        "SITETYPE": fields.String(
            required=True,
            description="Site Type (EMAP PROBablilty/EMAP/HAND-picked/STAR HAND-picked)",
        ),
        "REPEAT": fields.String(
            required=True, description="Was this a Repeat Visit (Y/blank)"
        ),
        "LON_DD": fields.String(
            required=True,
            description="Official Longitude in Decimal Degrees equal to  DLON_DD, or MLON_DD, or XLON_DD",
        ),
        "LAT_DD": fields.String(
            required=True,
            description="Official Latitude in Decimal Degrees equal to  DLON_DD, or MLON_DD, or XLON_DD",
        ),
        "XLON_DD": fields.String(
            required=True, description="X-site GPS Longitude - Decimal Degrees"
        ),
        "XLAT_DD": fields.String(
            required=True, description="X-site GPS Latitude - Decimal Degrees"
        ),
        "STRAHLER": fields.String(
            required=True, description="Strahler Order from RF3 Stream Data"
        ),
        "ST_ORDER": fields.String(
            required=True, description="RF3 STRAHLER ORDER CLASS"
        ),
        "DATE_COL": fields.String(required=True, description="Date of Site Visit"),
        "SITESAMP": fields.String(required=True, description="Was Site Sampled (Y/N)"),
        "FLOWSITE": fields.String(
            required=True,
            description="Target Class of Site (WADEABLE/BOATABLE/INTERRUPTED/WADEABLE/PARTIAL WADEABLE/PARTIAL BOATABLE/ALTERED)",
        ),
        "XSTATUS": fields.String(
            required=True, description="X-site Sampling Status Category"
        ),
        "VALXSTAT": fields.String(
            required=True, description="X-site Sampling Status Sub-Category"
        ),
        "TNT": fields.String(
            required=True,
            description="Site is a target stream (perennial/wadeable) or a non-target site",
        ),
        "STRATUM": fields.String(
            required=True, description="Stratum from the survey design for the site"
        ),
        "WGT_WSA": fields.String(
            required=True,
            description="Weight for statistical population estimation in km",
        ),
        "SAMPCHEM": fields.String(
            required=True,
            description="Chemistry Sample Collected - YES/NO/NA/PENDING ('NA'indicates chemistry sample lost or not analyzed)",
        ),
        "SAMPBENT": fields.String(
            required=True,
            description="Benthic Sample Collected - YES/NO/NA (NA indicates benthic sample low effort or not analyzed for WSA)",
        ),
        "SAMPPHAB": fields.String(
            required=True, description="Physical Habitat Sample Collected - YES/PENDING"
        ),
        "STATE": fields.String(required=True, description="State"),
        "COUNTY": fields.String(required=True, description="County"),
        "EPAREGION": fields.String(required=True, description="EPA Region"),
        "WESTEAST": fields.String(
            required=True,
            description="Site comes from EMAP-West (WEST) vs. WSA-east study (EAST)",
        ),
        "RT_WSA": fields.String(
            required=True,
            description="Reference Condition (ATH screen; R=Reference, S=Somewhat Disturbed, T=Highly Disturbed",
        ),
        "XELEV": fields.String(
            required=True, description="Elevation at the X-site (m)"
        ),
        "WSAREA": fields.String(
            required=True,
            description="Watershed Area Digitized from Maps (km2). Local Watershed Area if INTERBASIN TRANSFERS Noted in IM Comment",
        ),
        "ECO3": fields.String(required=True, description="Omernik Level 3 Ecoregion"),
        "ECO3_NM": fields.String(
            required=True, description="Omernik Level 3 Ecoregion Name"
        ),
        "ECOWSA9": fields.String(
            required=True, description="WSA Reporting Unit (9 aggregated ecoregions)"
        ),
        "ECOWSA3": fields.String(
            required=True,
            description="WSA Mega Reporting Unit (3 aggregated ecoregions)",
        ),
        "NAECO3": fields.String(
            required=True, description="North American Level 3 Ecoregion code"
        ),
        "NAECO2": fields.String(
            required=True, description="North American Level 2 Ecoregion code"
        ),
        "NAECO2_NM": fields.String(
            required=True, description="North American Level 2 Ecoregion Name"
        ),
        "NAECO1": fields.String(
            required=True, description="North American Level 1 Ecoregion code"
        ),
        "ECOREPORT": fields.String(
            required=True, description="Aggregated NAECO2 Name used for reporting"
        ),
        "HUC2": fields.String(
            required=True, description="2-digit HUC Catalog Unit Number"
        ),
        "HUC4": fields.String(
            required=True, description="4-digit HUC Catalog Unit Number"
        ),
        "HUC6": fields.String(
            required=True, description="6-digit HUC Catalog Unit Number"
        ),
        "HUC8": fields.String(
            required=True, description="8-digit HUC Catalog Unit Number"
        ),
        "HUC8_NM": fields.String(required=True, description="HUC Catalog Unit Name"),
        "IM_FLAG": fields.String(
            required=True, description="Flag assigned during data validation"
        ),
        "IM_COMMENT": fields.String(
            required=True, description="Comments regarding data validation"
        ),
    },
)

detail_0405_point_feature = ns.model(
    "0405 Point Feature",
    {
        "type": fields.String(required=True, default="Feature"),
        "geometry": fields.Nested(point, required=True),
        "properties": fields.Nested(detail_props_0405),
    },
)


nlcd_category = ns.model(
    "NLCD Feature Categories",
    {
        "PctOwWs": fields.Float,
        "PctIceWs": fields.Float,
        "PctUrbOpWs": fields.Float,
        "PctUrbLoWs": fields.Float,
        "PctUrbMdWs": fields.Float,
        "PctUrbHiWs": fields.Float,
        "PctBlWs": fields.Float,
        "PctDecidWs": fields.Float,
        "PctConifWs": fields.Float,
        "PctMxFstWs": fields.Float,
        "PctShrbWs": fields.Float,
        "PctGrsWs": fields.Float,
        "PctHayWs": fields.Float,
        "PctCropWs": fields.Float,
        "PctWdWetWs": fields.Float,
        "PctHbWetWs": fields.Float,
    },
)

chart_category = ns.model(
    "NLCD Chart Category",
    {
        "category": fields.String,
        "start": fields.Float,
        "width": fields.Float,
    },
)

nlcd_feature = ns.model(
    "NLCD Feature Properties",
    {
        "SITE_ID": fields.String(read_only=True),
        "COMID": fields.Integer(
            desciption="Unique ID of NHDPlusV2 catchment that SITE_ID is found"
        ),
        "WsAreaSqKm": fields.Float,
        "WsPctFull": fields.Float,
        "categories": fields.Nested(nlcd_category, required=True),
    },
)

compare_year = ns.model(
    "NLCD Year Categories",
    {
        "year": fields.String(),
        "categories": fields.List(fields.Nested(chart_category, required=True)),
    },
)

compare_feature = ns.model(
    "NLCD Comparable Categories",
    {
        "comparable": fields.List(fields.Nested(compare_year), required=True),
        "square_list": fields.List(fields.String()),
    },
)

category_feature = ns.model(
    "NLCD Yearly Category",
    {
        "2001": fields.Float,
        "2004": fields.Float,
        "2006": fields.Float,
        "2011": fields.Float,
        "2013": fields.Float,
        "2016": fields.Float,
        "2019": fields.Float,
    },
)


#  multipolygon_feature = ns.model(
#      "MultiPolygon Feature",
#      {
#          "type": fields.String(default="Feature", require=True),
#          "geometry": fields.Nested(multipolygon, required=True),
#          "properties": fields.Nested(epa_props),
#      },
#  )
