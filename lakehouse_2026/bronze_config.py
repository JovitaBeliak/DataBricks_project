BASE_PATH = "/Volumes/workspace/bronze/source_systems"

INGESTION_CONFIG = [
    #ERP
    {
        "source": "ern",
        "path": f"{BASE_PATH}/source_erp/CUST_AZ12.csv",
        "table": "erp_cust_az12"
    },
    {
        "source": "ern",
        "path": f"{BASE_PATH}/source_erp/LOC_A101.csv",
        "table": "erp_loc_a101"
    },
    {
        "source": "ern",
        "path": f"{BASE_PATH}/source_erp/PX_CAT_G1V2.csv",
        "table": "erp_px_cat_g1v2"
    }
]