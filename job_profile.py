from collections import OrderedDict



ACROPOLIS_NAHV_JPS_MASTER = {
    "NAHV-GOS": [
       # {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WVT_1_master",
       #  "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os",
       #  "category": 'reg-handedover', "JP_ID": "5e3a657dd24d8234685553f9", "FQA": "bhawani.singh@nutanix.com"},
       # {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WI_1_master",
       # "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os",
       # "category": 'reg-handedover', "JP_ID": "5daff2857b48b18055b0a426", "FQA": "bhawani.singh@nutanix.com"},

      # {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WLC_new1_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5ee9bef48e79ce8896ce24ac", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LLC_New1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5ee9c8f08e79ce6361d09af0", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WVDT_New1_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5ee9ecd0d24d8210af0a5b22", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LVDT_new1_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5ee9f3908e79ce887f7468ab", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LVDT_new2_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "ahv-guest-os",  "category": 'reg-handedover', "JP_ID": "5ee9f4b4d24d822740ed17f1", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LVDT_new3_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5eec7d828e79ce6361d13e86", "FQA": "bhawani.singh@nutanix.com"},

      #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LI_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5daeacc17b48b161d5baf1dd", "FQA": "bhawani.singh@nutanix.com"},
       #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WLC_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5db167d97b48b1eeff499ed4", "FQA": "bhawani.singh@nutanix.com"},
       # {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LLC_1_master", "throttle": [u"throttle_tests__10"], "max_dep": [u'max_deployments__10'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5db270747b48b15a59879f4c", "FQA": "bhawani.singh@nutanix.com"},
       #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LVDT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc8f9de7b48b1361648b047", "FQA": "bhawani.singh@nutanix.com"},
       #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WVDT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc926887b48b106a29b144d", "FQA": "bhawani.singh@nutanix.com"},
    ],
    "NAHV-PC": [
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_FEAT_6387_RBAC_Nested_master", "throttle": [u"throttle_tests__2"], "max_dep": [u'max_deployments__2'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e4e4efad24d825d1dbd95ed", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_Metropolis_Nested", "throttle": [u"throttle_tests__2"], "max_dep": [u'max_deployments__2'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5cc92cea7b48b1ae8a54b918", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Uhura_GuestCustomization_UI_Nested_master", "throttle": [u"throttle_tests__2"], "max_dep": [u'max_deployments__2'], "sub-component": "uhura-ui", "category": 'reg-handedover', "JP_ID": "5e22fd48d24d82c29416552b", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Uhura_GuestCustomization_REST_Nested_master", "throttle": [u"throttle_tests__2"], "max_dep": [u'max_deployments__2'], "sub-component": "uhura-rest", "category": 'reg-handedover', "JP_ID": "5e202402d24d826a0b6c9434", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Uhura_FEAT-6978_v3_clone_Nested_master", "throttle": [u"throttle_tests__2"], "max_dep": [u'max_deployments__2'], "sub-component": "uhura-clone", "category": 'reg-handedover', "JP_ID": "5e2023cbd24d82df7c62391f", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_Metropolis_xi_Nested_master", "throttle": [u"throttle_tests__2"], "max_dep": [u'max_deployments__2'], "sub-component": "metropolis-xi", "category": 'reg-handedover', "JP_ID": "5e1c8ed38e79ce195eb42e57", "FQA": "bhawani.singh@nutanix.com"},

        {"branch": "master", "rdm_v": ["rdm__virtual"],"JP_NAME": "Regression_Acropolis_MTS_Nutest_RBAC_snapshot_api_nested_master", "throttle": [u"throttle_tests__2"],"max_dep": [u'max_deployments__2'], "sub-component": "rbac-api", "category": 'reg-handedover',"JP_ID": "5ef0dac42bc0c465e171c034", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"],"JP_NAME": "Regression_Acropolis_MTS_Nutest_RBAC_SNAPSHOT_nested-master", "throttle": [u"throttle_tests__2"],"max_dep": [u'max_deployments__2'], "sub-component": "rbac-snapshot", "category": 'reg-handedover',"JP_ID": "5ef0db2f2bc0c4729145a8fe", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"],"JP_NAME": "Regression_Acropolis_MTS_Nutest_OVA_RBAC_nested-master","throttle": [u"throttle_tests__2"],"max_dep": [u'max_deployments__2'], "sub-component": "ova-rbac", "category": 'reg-handedover',"JP_ID": "5ef0db912bc0c4387f5de314", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"],"JP_NAME": "Regression_Acropolis_MTS_Nutest_OVA_AHV_AHV_Nested","throttle": [u"throttle_tests__7"],"max_dep": [u'max_deployments__7'], "sub-component": "ova-ahv", "category": 'reg-handedover',"JP_ID": "5ef0dbf48e79cea1f19be6ce", "FQA": "bhawani.singh@nutanix.com"},



    ],

    "NAHV-CATALOG-PE": [
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_PE_Nested_master", "throttle": [u"throttle_tests__4"], "max_dep": [u'max_deployments__4'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e402b4a8e79ce6411a50ef8", "FQA": "bhawani.singh@nutanix.com"}
    ],
    "NAHV-CATALOG-PC": [
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5efdb8db8e79ceb94f05a30b", "FQA": "bhawani.singh@nutanix.com"},

        # {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_7112_np_Catalog_Nested_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e2e4c362bc0c406b53c2c15", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Nested_master", "throttle": [u"throttle_tests__10"], "max_dep": [u'max_deployments__10'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e402dbcd24d82de4de7f545", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_Nested_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e4d07f42bc0c466b77aac34", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_Nested_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__5'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e4d081f2bc0c466a452ee65", "FQA": "bhawani.singh@nutanix.com"}
    ],
    "NAHV-PE": [
        {"branch": "master", "rdm_v": ["rdm__virtual"],"JP_NAME": "Regression_Ergon_without_NS_master", "throttle": [u"throttle_tests__2"],"max_dep": [u'max_deployments__2'], "sub-component": "ergon", "category": 'reg-handedover',"JP_ID": "5f50a859d24d8217bbb12c3e", "FQA": "bhawani.singh@nutanix.com"},

        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_AHV_Mgmt_Acli_1_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e21ee44d24d82df763a4a70", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Uhura__AHV__REST_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e200071d24d82df815b7a22", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Uhura__AHV__RPC_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e200143d24d82df8a678ee5", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_Uhura_Audit_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e1c8bb38e79ce222a5ba7f7", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e1c8c2d2bc0c45737042d7f", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_Webhooks_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e1c8d6f8e79ce1956c0b196", "FQA": "bhawani.singh@nutanix.com"},
    ],
    "NAHV-SCHEDULER": [
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Nested_master", "throttle": [u"throttle_tests__3"], "max_dep": [u'max_deployments__3'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e1fae488e79ce1956c17c38", "FQA": "bhawani.singh@nutanix.com"}
    ],
    "NAHV-UI": [
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "master_pe_nahv", "throttle": [u"throttle_tests__20"], "max_dep": [u'max_deployments__20'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5d11b4187b48b19a8dc6e9e1", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Uhura__AHV__UI_Nested_master", "throttle": [u"throttle_tests__2"], "max_dep": [u'max_deployments__2'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5e20035c8e79ce1943ac70bc", "FQA": "bhawani.singh@nutanix.com"}
    ],

}



ACROPOLIS_JPS_5_18 = {
    "NAHV-GOS": [
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LI_1_Nested_5.18", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5ec63d888e79ce43bcca3c25", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WI_1_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5daff2857b48b18055b0a426", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WLC_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5db167d97b48b1eeff499ed4", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LLC_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5db270747b48b15a59879f4c", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LVDT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc8f9de7b48b1361648b047", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WVDT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc926887b48b106a29b144d", "FQA": "bhawani.singh@nutanix.com"},
        #{"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WVT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc926887b48b106a29b144d", "FQA": "bhawani.singh@nutanix.com"}
    ]}



ACROPOLIS_JPS_5_15_1 = {

"NAHV-GOS": [
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LI_1_Nested_5.18", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5ec63d888e79ce43bcca3c25", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WI_1_master", "throttle": [u"throttle_tests__5"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5daff2857b48b18055b0a426", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WLC_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5db167d97b48b1eeff499ed4", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LLC_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5db270747b48b15a59879f4c", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_LVDT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc8f9de7b48b1361648b047", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WVDT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc926887b48b106a29b144d", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "rdm_v": ["rdm__virtual"], "JP_NAME": "Regression_Acropolis_NAHV_Guest_OS_WVT_1_master", "throttle": [u"throttle_tests__7"], "max_dep": [u'max_deployments__7'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5dc926887b48b106a29b144d", "FQA": "bhawani.singh@nutanix.com"}
    ]
}

BRANCH_METADATA = {"MASTER": ACROPOLIS_NAHV_JPS_MASTER,
                   "5.19": ACROPOLIS_NAHV_JPS_MASTER,
                   "5.15.1": ACROPOLIS_JPS_5_15_1}



ACROPOLIS_JPS_MASTER = {
    "NO-PC": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_AOS_NS_master", "max_dep": [u'max_deployments__1'], "sub-component": "aos-ns", "category": 'reg-handedover', "JP_ID": "5b21e7c81b54d06cac30d337", "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_master", "max_dep": [u'max_deployments__1'], "sub-component": "vm-management", "category": 'reg-handedover', "JP_ID": "5a7846c61b54d091b9237664", "FQA": ["velurusruthi.naidu@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_V3_Vm_Management_master", "max_dep": [u'max_deployments__1'], "sub-component": "v3-vm-management", "category": 'reg-handedover', "JP_ID": "5a784ace1b54d0924ebe647e", "FQA": ["sonny.li@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Webhooks_master", "max_dep": [u'max_deployments__1'], "sub-component": "webhooks", "category": 'reg-handedover', "JP_ID": "5a58a0c71b54d0d648d262b1", "FQA": ["raymond.yip@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_CO_AOS_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-co", "category": 'reg-handedover', "JP_ID": "5c764fd292491e26d6b7cfc2", "FQA": ["robert@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_ACLI_Scheduling_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler-acli", "category": 'reg-handedover', "JP_ID": "5dad84267b48b152f04ceafd", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Storage_Persona_master", "max_dep": [u'max_deployments__1'], "sub-component": "storage-persona", "category": 'reg-handedover', "JP_ID": "5d80f2cf7b48b124845eae98", "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]}
    ],
    "SCHEDULER": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Ads_HA_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5a58a0431b54d0e2af8b3bd7", "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5a58a09d1b54d0e2cbb927d3", "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5bff8c4e114cdb568e35b365", "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]},
    ],
    "SCHEDULER-OPT": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_1_master", "max_dep": [u'max_deployments__5'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5da01c2a7b48b1571f2feacd", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5dabd8b97b48b14d4a0f6d5b", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_3_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5dabdb037b48b1268dfe3644", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_HA_Set_1_master", "max_dep": [u'max_deployments__10'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5da4153a7b48b173182adb22", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_HA_Set_2_master", "max_dep": [u'max_deployments__2'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5dac6baa7b48b18f717fa49d", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_HA_Set_3_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5dacdcbf7b48b10cc26f3823", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Ads_Set_1_master", "max_dep": [u'max_deployments__5'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5da417f07b48b1853590cd55", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Ads_Set_2_master", "max_dep": [u'max_deployments__2'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5dabde957b48b1759970af83", "FQA": ["dipika.darshan@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_Set_1_master", "max_dep": [u'max_deployments__2'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5dacdf8c7b48b10cc26f3854", "FQA": ["dipika.darshan@nutanix.com"]},
    ],
    "NO-PC-HA": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_HA_Twonode_master", "max_dep": [u'max_deployments__1'], "sub-component": "scheduler", "category": 'reg-handedover', "JP_ID": "5b14d89c1b54d0524c617c7b", "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]}
    ],
    "GUEST-OS-OTHERS": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_AHV_NS_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-ns", "category": 'reg-handedover', "JP_ID": "5ab4f76e1b54d04f98bdaceb", "FQA": ["dli@nutanix.com", "bruce.gao@nutanix.com", "velurusruthi.naidu@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_api_stress_general_master", "max_dep": [u'max_deployments__1'], "sub-component": "api-stress", "category": 'reg-handedover', "JP_ID": "5ab223321b54d00c0a9e0cf2", "FQA": ["dli@nutanix.com", "bruce.gao@nutanix.com", "velurusruthi.naidu@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Frodo_master", "max_dep": [u'max_deployments__5'], "sub-component": "frodo", "category": 'reg-handedover', "JP_ID": "5a589eb11b54d0e2af8b3bd5", "FQA": ["dli@nutanix.com", "bruce.gao@nutanix.com", "velurusruthi.naidu@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_CO_AHV_master", "max_dep": [u'max_deployments__3'], "sub-component": "ahv-co", "category": 'reg-handedover', "JP_ID": "5c76657b92491e26d6b7cfc4", "FQA": ["robert@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_master", "max_dep": [u'max_deployments__1'], "sub-component": "vnuma", "category": 'reg-handedover', "JP_ID": "5c7f7a207b48b1be9b2eec16", "FQA": ["dli@nutanix.com", "bruce.gao@nutanix.com", "velurusruthi.naidu@nutanix.com"]}
    ],
    "GUEST-OS-OPT": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_1_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b65987b48b1e881694e5b", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b66107b48b1ec81ce058a", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_3_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b663c7b48b1ea654b8f2f", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_4_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b668f7b48b1f0c1249c8a", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_5_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b680c7b48b1f95ac37469", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_6_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b685d7b48b1fdd8ed2db1", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_1_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b68ac7b48b1fcbe54eca5", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7cd5a27b48b152d3fa2d24", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WI_1_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b68d57b48b1fdd8ed2e18", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WI_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7d10e57b48b1c16e02ab03", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LI_1_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b690a7b48b1fe3e9e1735", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LI_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6a157b48b1073d77ccc3", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LI_3_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6a3c7b48b10651cbad74", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_1_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6b737b48b10ebf9431c1", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6bc37b48b10070fec1ec", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_3_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6bf17b48b10ebf9431c5", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_4_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6c107b48b10a1c7ec7af", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_5_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6c447b48b1073d77cce1", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_6_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6c5d7b48b1168bf48e2a", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_7_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6c917b48b1185b2d72d0", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_1_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6cec7b48b10ebf9431ce", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6d057b48b11a9e7e9399", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_1_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7b6d557b48b11a9e7e93a0", "FQA": "bhawani.singh@nutanix.com"},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_2_master", "max_dep": [u'max_deployments__1'], "sub-component": "ahv-guest-os", "category": 'reg-handedover', "JP_ID": "5d7d135e7b48b1e941948339", "FQA": "bhawani.singh@nutanix.com"}
    ],
    "PC": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_batch_vm_pc_master", "max_dep": [u'max_deployments__1'], "sub-component": "batch-vms", "category": 'reg-handedover', "JP_ID": "5aebc3321b54d04721d5b8c8", "FQA": ["sonny.li@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_master", "max_dep": [u'max_deployments__1'], "sub-component": "batch-vms", "category": 'reg-handedover', "JP_ID": "5aebfa3e1b54d0bf1eceabac", "FQA": ["sonny.li@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Metropolis_xi_master", "max_dep": [u'max_deployments__1'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5b156ea41b54d0f49b33b3b3", "FQA": ["sai.vishalk@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Metropolis_master", "max_dep": [u'max_deployments__1'], "sub-component": "metropolis", "category": 'reg-handedover', "JP_ID": "5ab228c51b54d007e04fdbc1", "FQA": ["sai.vishalk@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Audit_master", "max_dep": [u'max_deployments__1'], "sub-component": "audit", "category": 'reg-handedover', "JP_ID": "5bb207f3114cdbae455754d6", "FQA": ["syam.mohan@nutanix.com"]}
    ],
    "SCALEOUT-PC": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_VMS_Rolling_Group_ScaleOutPC_master", "max_dep": [u'max_deployments__1'], "sub-component": "scaleout-pc", "category": 'reg-handedover', "JP_ID": "5db1013f7b48b1519a91bd1e", "FQA": ["sonny.li@nutanix.com"]}

    ],
    "PC-CATALOG":[
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_master", "max_dep": [u'max_deployments__1'], "JP_ID": "5cee8d657b48b1035bc8c54b", "FQA": ["saurabh.dohare@nutanix.com"], "sub-component": "catalog", "category": 'reg-handedover'},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_master", "max_dep": [u'max_deployments__3'], "JP_ID": "5d11ddd77b48b13bf30e0959", "FQA": ["saurabh.dohare@nutanix.com"], "sub-component": "catalog", "category": 'reg-handedover'},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_master", "max_dep": [u'max_deployments__2'], "JP_ID": "5d11d1277b48b19a8dc6eb4f", "FQA": ["saurabh.dohare@nutanix.com"], "sub-component": "catalog", "category": 'reg-handedover'}
    ],
    "PC-CATALOG-HYPERVISOR-ANY":[
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_master", "max_dep": [u'max_deployments__6'], "JP_ID": "5ab20abf1b54d0f669f4f4be", "FQA": ["saurabh.dohare@nutanix.com"], "sub-component": "catalog", "category": 'reg-handedover'}
    ],
    "PC-CATALOG-ESX-HYPERVISOR-ANY": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_Esx_Master", "max_dep": [u'max_deployments__1'], "JP_ID": "5dc90ba87b48b1b05fbbacdb", "FQA": ["saurabh.dohare@nutanix.com"], "sub-component": "catalog", "category": 'reg-handedover'}
    ],
    "GPU": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_master", "max_dep": [u'max_deployments__1'], "sub-component": "gpu", "category": 'reg-handedover', "JP_ID": "5a58a1081b54d0ddd9cb638a", "FQA": ["kern.qian@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_VGpu_master", "max_dep": [u'max_deployments__1'], "sub-component": "gpu", "category": 'reg-handedover', "JP_ID": "5a58a1e21b54d0ca7acd9973", "FQA": ["kern.qian@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_master", "max_dep": [u'max_deployments__1'], "sub-component": "gpu", "category": 'reg-handedover', "JP_ID": "5c750df37b48b1577b0a1c5a", "FQA": ["kern.qian@nutanix.com"]}
    ],
    "VNUMA": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Vnuma_master", "max_dep": [u'max_deployments__1'], "sub-component": "vnuma", "category": 'reg-handedover', "JP_ID": "5a589ee81b54d0e2cbb927d1", "FQA": ["robert@nutanix.com"]},
     ],
    "Xi-MGMT": [
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6906_master", "max_dep": [u'max_deployments__1'], "sub-component": "xi-manageability", "category": 'reg-handedover', "JP_ID": "5d5e300e7b48b1e4e14fb98b", "FQA": ["victor.kamanga@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_Xi_Telemetry_FEAT_4361_master", "max_dep": [u'max_deployments__1'], "sub-component": "xi-manageability", "category": 'reg-handedover', "JP_ID": "5d5e31117b48b12ef8da1f9b", "FQA": ["victor.kamanga@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6626_master", "max_dep": [u'max_deployments__1'], "sub-component": "xi-manageability", "category": 'reg-handedover', "JP_ID": "5d5e31f77b48b1dd730641c4", "FQA": ["victor.kamanga@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Pairing_API_master", "max_dep": [u'max_deployments__1'], "sub-component": "xi-manageability", "category": 'reg-handedover', "JP_ID": "5d5e335d7b48b1de13a8c619", "FQA": ["victor.kamanga@nutanix.com"]},
        {"branch": "master", "JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Pairing_OP-xi_API_master", "max_dep": [u'max_deployments__1'], "sub-component": "xi-manageability", "category": 'reg-handedover', "JP_ID": "5d5e33fd7b48b12f4eb24f28", "FQA": ["victor.kamanga@nutanix.com"]},
    ]
}




ACROPOLIS_JPS_NON_REG_HANDEDOVER = {
    "PC": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_OVA_RBAC_master", "max_dep": [u'max_deployments__1'], "sub-component": "ova-ovf", "category": 'non-reg-handedover', "JP_ID": "5d774b9d7b48b1e368b2cf5f", "FQA": ["nagasuri.sree@nutanix.com"]},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_OVA_AHV_AHV_master", "max_dep": [u'max_deployments__3'], "sub-component": "ova-ovf", "category": 'non-reg-handedover', "JP_ID": "5cb45fdf7b48b1f0b1d52d79", "FQA": ["syam.mohan@nutanix.com"]},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Capabilities_master", "max_dep": [u'max_deployments__1'], "sub-component": "capabilities", "category": 'non-reg-handedover', "JP_ID": "5d4ac2dd7b48b1d7b3a1a863", "FQA": ["vistaar.juneja@nutanix.com"]},
    ],
    "PC-OVA": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_OVA_AHV_ESX_master", "max_dep": [u'max_deployments__3'], "sub-component": "ova-ovf", "category": 'non-reg-handedover', "JP_ID": "5cb45d4a7b48b1f0b1d52d64", "FQA": ["syam.mohan@nutanix.com"]},
    ],
    # "NO-PC":[
    #     {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Storage_Persona_master", "max_dep": [u'max_deployments__5'], "sub-component": "storage-persona", "category": 'non-reg-handedover', "JP_ID": "5d80f2cf7b48b124845eae98", "FQA": ["dipika.darshan@nutanix.com", "maksim.kalitinenkov@nutanix.com"]},
    # ]
}


# ACROPOLIS_JPS_AMD_MASTER = {
# 'GPU': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_AMD_Qual_master'), ('sub-component', 'gpu'), ('JP_ID', u'5dd7a354d24d82bb6e5e1f84'), ('max_dep', [u'max_deployments__1'])]),
#          OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_AMD_Qual_master'), ('sub-component', 'gpu'), ('JP_ID', u'5dd7a357d24d82bb6c54861d'), ('max_dep', [u'max_deployments__1'])]),
#          OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_AMD_Qual_master'), ('sub-component', 'gpu'), ('JP_ID', u'5dd7a358d24d82bb578d9250'), ('max_dep', [u'max_deployments__1'])])],
#  'GUEST-OS-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_1_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a366d24d82bb6d72fae0'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_2_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3682bc0c408db3ef3bc'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_3_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a36a7b48b1cbecec832f'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_4_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a36cd24d82bb69bffd22'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_5_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a36e2bc0c408eb77143f'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_6_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a36f7b48b1cbe37c02ca'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_1_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3718e79ce8ec02df311'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_2_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3732bc0c408ec9e0628'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_1_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a375d24d82bb67d6494c'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_2_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3768e79ce8ec296d01e'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_1_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3788e79ce8eb0c23ad4'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_2_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a37a2bc0c408e2757ded'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_3_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a37cd24d82bb73d7a810'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_1_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a37d8e79ce8ebacc992f'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_2_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a37fd24d82bb6e5e1f8f'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_3_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3812bc0c408ed4ef427'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_4_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3838e79ce8eaeb5e9c6'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_5_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3858e79ce8eb829f520'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_6_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3868e79ce8eaa468bab'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_7_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3897b48b1cbee004f37'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_1_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a38b8e79ce8ebacc9933'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_2_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a38c7b48b1cbe60a76ee'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_1_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a38ed24d82bb6e5e1f93'), ('max_dep', [u'max_deployments__1'])]),
#                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_2_AMD_Qual_master'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dd7a3907b48b1cbd72d0d53'), ('max_dep', [u'max_deployments__1'])])],
#  'GUEST-OS-OTHERS': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_AMD_Qual_master'), ('sub-component', 'ahv-ns'), ('JP_ID', u'5dd7a33c8e79ce8eca1f5dc9'), ('max_dep', [u'max_deployments__1'])]),
#                      OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_AMD_Qual_master'), ('sub-component', 'api-stress'), ('JP_ID', u'5dd7a33e8e79ce8ec808b68d'), ('max_dep', [u'max_deployments__1'])]),
#                      OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_AMD_Qual_master'), ('sub-component', 'frodo'), ('JP_ID', u'5dd7a340d24d82bb62d3a55c'), ('max_dep', [u'max_deployments__5'])]),
#                      OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_AMD_Qual_master'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dd7a3428e79ce8eb7f490e8'), ('max_dep', [u'max_deployments__3'])]),
#                      OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_AMD_Qual_master'), ('sub-component', 'vnuma'), ('JP_ID', u'5dd7a3448e79ce8eb829f51b'), ('max_dep', [u'max_deployments__1'])])],
#  'NO-PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_AMD_Qual_master'), ('sub-component', 'aos-ns'), ('JP_ID', u'5dd7a3472bc0c408d9ea1987'), ('max_dep', [u'max_deployments__1'])]),
#            OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_AMD_Qual_master'), ('sub-component', 'vm-management'), ('JP_ID', u'5dd7a3498e79ce8eb9fb7dd2'), ('max_dep', [u'max_deployments__1'])]),
#            OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_AMD_Qual_master'), ('sub-component', 'v3-vm-management'), ('JP_ID', u'5dd7a34b2bc0c408e45f7e38'), ('max_dep', [u'max_deployments__1'])]),
#            OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_AMD_Qual_master'), ('sub-component', 'webhooks'), ('JP_ID', u'5dd7a34d2bc0c408e887cef6'), ('max_dep', [u'max_deployments__1'])]),
#            OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_AMD_Qual_master'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dd7a34fd24d82bb64cbb5d4'), ('max_dep', [u'max_deployments__1'])]),
#            OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_ACLI_Scheduling_AMD_Qual_master'), ('sub-component', 'scheduler-acli'), ('JP_ID', u'5dd7a351d24d82bb6e5e1f81'), ('max_dep', [u'max_deployments__1'])]),
#            OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Storage_Persona_AMD_Qual_master'), ('sub-component', 'storage-persona'), ('JP_ID', u'5dd7a3527b48b1cbdef54a31'), ('max_dep', [u'max_deployments__1'])])],
#  'NO-PC-HA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a346d24d82bb59a22cd5'), ('max_dep', [u'max_deployments__1'])])],
#  'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_AMD_Qual_master'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dd7a333d24d82bb59a22cd0'), ('max_dep', [u'max_deployments__1'])]),
#         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_AMD_Qual_master'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dd7a3342bc0c408eac0cfe5'), ('max_dep', [u'max_deployments__1'])]),
#         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_AMD_Qual_master'), ('sub-component', 'metropolis'), ('JP_ID', u'5dd7a336d24d82bb578d9248'), ('max_dep', [u'max_deployments__1'])]),
#         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_AMD_Qual_master'), ('sub-component', 'metropolis'), ('JP_ID', u'5dd7a3387b48b1cbee004f31'), ('max_dep', [u'max_deployments__1'])]),
#         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_AMD_Qual_master'), ('sub-component', 'audit'), ('JP_ID', u'5dd7a33ad24d82bb5f9d6786'), ('max_dep', [u'max_deployments__1'])])],
#  'PC-CATALOG': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_AMD_Qual_master'), ('sub-component', 'catalog'), ('JP_ID', u'5dd7a32bd24d82bb5ca86884'), ('max_dep', [u'max_deployments__1'])]),
#                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_AMD_Qual_master'), ('sub-component', 'catalog'), ('JP_ID', u'5dd7a32d2bc0c408f1552ca8'), ('max_dep', [u'max_deployments__3'])]),
#                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_AMD_Qual_master'), ('sub-component', 'catalog'), ('JP_ID', u'5dd7a32fd24d82bb62d3a556'), ('max_dep', [u'max_deployments__2'])])],
#  'PC-CATALOG-HYPERVISOR-ANY': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_AMD_Qual_master'), ('sub-component', 'catalog'), ('JP_ID', u'5dd7a3312bc0c408e008d333'), ('max_dep', [u'max_deployments__6'])])],
#  'SCHEDULER-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_1_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a392d24d82bb633579e2'), ('max_dep', [u'max_deployments__5'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_2_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a3942bc0c408eb771445'), ('max_dep', [u'max_deployments__1'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_3_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a3978e79ce8eb2239add'), ('max_dep', [u'max_deployments__1'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_1_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a398d24d82bb5ca868a0'), ('max_dep', [u'max_deployments__10'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_2_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a39ad24d827a6273a8a6'), ('max_dep', [u'max_deployments__2'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_3_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a39dd24d82bb74206caf'), ('max_dep', [u'max_deployments__1'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_1_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a39ed24d82bb6e5e1f97'), ('max_dep', [u'max_deployments__5'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_2_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a3a08e79ce8ebe843bbb'), ('max_dep', [u'max_deployments__2'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_Set_1_AMD_Qual_master'), ('sub-component', 'scheduler'), ('JP_ID', u'5dd7a3a38e79ce8ebb128e34'), ('max_dep', [u'max_deployments__2'])])],
#  'VNUMA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_AMD_Qual_master'), ('sub-component', 'vnuma'), ('JP_ID', u'5dd7a35a8e79ce8ec296d018'), ('max_dep', [u'max_deployments__1'])])],
#  'Xi-MGMT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6906_AMD_Qual_master'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dd7a35cd24d82bb578d9252'), ('max_dep', [u'max_deployments__1'])]),
#              OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Xi_Telemetry_FEAT_4361_AMD_Qual_master'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dd7a35dd24d82bb70d3121e'), ('max_dep', [u'max_deployments__1'])]),
#              OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6626_AMD_Qual_master'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dd7a3608e79ce8eb6a49715'), ('max_dep', [u'max_deployments__1'])]),
#              OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_API_AMD_Qual_master'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dd7a361d24d82bb715e1f88'), ('max_dep', [u'max_deployments__1'])]),
#              OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_OP-xi_API_AMD_Qual_master'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dd7a3642bc0c408d69a83c7'), ('max_dep', [u'max_deployments__1'])])]
#  }


UHURA_JPS_MASTER = {
    "PC": [
        {"JP_NAME": "Regression_Uhura_FEAT-6978_v3_clone_master", "max_dep": [u'max_deployments__1'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b75519f1b54d0c24d176aba", "FQA": ["saurabh.jain@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura_GuestCustomization_master", "max_dep": [u'max_deployments__3'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5a77fbbc1b54d017d555d198", "FQA": ["saurabh.jain@nutanix.com"]}
    ],
    "NO-PC-WITH-VC": [
        {"JP_NAME": "Regression_Uhura__ESX__RPC_master", "max_dep": [u'max_deployments__3'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b050eef1b54d080995ca162", "FQA": ["saurabh.jain@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__ESX__REST_master", "max_dep": [u'max_deployments__2'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b0257bd1b54d034531dab47", "FQA": ["saurabh.jain@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__ESX__UI_master", "max_dep": [u'max_deployments__1'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b025e8f1b54d08318f7ca97", "FQA": ["nagasuri.sree@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__ManagementServer_master", "max_dep": [u'max_deployments__2'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b0259bc1b54d03bd372cb75", "FQA": ["saurabh.jain@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura_FEAT-3370_master", "max_dep": [u'max_deployments__1'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b7560d11b54d0d2336851c5", "FQA": ["saurabh.jain@nutanix.com"]}
    ],
    "NO-PC-NO-VC": [
        {"JP_NAME": "Regression_Uhura__AHV__REST_master", "max_dep": [u'max_deployments__1'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b0255bc1b54d04447a93b5c", "FQA": ["saurabh.jain@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__AHV__RPC_master", "max_dep": [u'max_deployments__2'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "58c90c0e1b54d02d9ad69669", "FQA": ["saurabh.jain@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__AHV__UI_master", "max_dep": [u'max_deployments__1'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5b025d531b54d082017341d4", "FQA": ["saurabh.jain@nutanix.com"]}
    ],
    "NS-WITH-VC": [
        {"JP_NAME": "Regression_Uhura_GoldSuite_NS_master", "max_dep": [u'max_deployments__1'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "59e5ce401b54d09abcef97e9", "FQA": ["saurabh.jain@nutanix.com"]}
    ],
    "NS-NO-VC": [
        {"JP_NAME": "Regression_Uhura__Ergon__NS_master", "max_dep": [u'max_deployments__1'], "sub-component": "uhura", "category": 'reg-handedover', "JP_ID": "5aea79f91b54d01d50f0531b", "FQA": ["saurabh.jain@nutanix.com"]}
    ]
}


# UHURA_JPS_AMD_MASTER = {
#     'NO-PC-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__REST_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a59c7b48b1cbe01eda7e'), ('max_dep', [u'max_deployments__1'])]),
#                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__RPC_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a59ed24d82bb563ece4a'), ('max_dep', [u'max_deployments__2'])]),
#                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__UI_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5a08e79ce8ebda1b5c8'), ('max_dep', [u'max_deployments__1'])])],
#  'NO-PC-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__RPC_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5937b48b1cbd20ee1c2'), ('max_dep', [u'max_deployments__3'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__REST_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5958e79ce8ebda1b5c5'), ('max_dep', [u'max_deployments__2'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__UI_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5978e79ce8ec296d06d'), ('max_dep', [u'max_deployments__1'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ManagementServer_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5997b48b1cbe8fae0f4'), ('max_dep', [u'max_deployments__2'])]),
#                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-3370_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a59ad24d82bb63357a48'), ('max_dep', [u'max_deployments__1'])])],
#  'NS-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__Ergon__NS_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5a77b48b1cbda967b9b'), ('max_dep', [u'max_deployments__1'])])],
#  'NS-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GoldSuite_NS_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5a5d24d82bb67d649b5'), ('max_dep', [u'max_deployments__1'])])],
#  'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5a12bc0c408e1e828d5'), ('max_dep', [u'max_deployments__1'])]),
#         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GuestCustomization_AMD_Qual_master'), ('sub-component', 'uhura'), ('JP_ID', u'5dd7a5a32bc0c408deb5c88c'), ('max_dep', [u'max_deployments__3'])])]
#  }


GOLD_SUITE_JPS = {
    "NO-PC": [
        {"JP_NAME": "AHV_Regression_HA_Scheduler_GoldSuite", "max_dep": [u'max_deployments__3'], "JP_ID": "5c20a7b1114cdb675645c466", "sub-component": "scheduler", "category": 'reg-handedover'},
        {"JP_NAME": "AHV_Regression_GuestOS_GoldSuite", "max_dep": [u'max_deployments__3'], "JP_ID": "5c20a814114cdb8288eb097a", "sub-component": "guest_os", "category": 'reg-handedover'}
    ],
    "GPU": [
        {"JP_NAME": "AHV_Regression_GPU_GoldSuite", "max_dep": [u'max_deployments__3'], "JP_ID": "5c22f874114cdb0f6e2ae5c6", "sub-component": "gpu", "category": 'reg-handedover'}
    ],
    "UHURA": [
        {"JP_NAME": "AHV_Regression_Uhura_GoldSuite", "max_dep": [u'max_deployments__3'], "JP_ID": "5c1cb9ca114cdbedcd2d162c", "sub-component": "uhura", "category": 'reg-handedover'}
    ],
    "PC": [
        {"JP_NAME": "AHV_Regression_Catalog_GoldSuite", "max_dep": [u'max_deployments__3'], "JP_ID": "5c20ad4a114cdb9c8b89a2b2", "sub-component": "catalog", "category": 'catalog'}
    ]
}

ACROPOLIS_JPS_LTS_5_5_8 = {
    "NO-PC": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.5.8", "JP_ID": "5bd3616943d9d3385db970a1"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Ads_HA_5.5.8", "JP_ID": "5bd3616943d9d3391617f73d"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.5.8", "JP_ID": "5bd3616943d9d3387ce37a22"},
        {"JP_NAME": "Regression_Acropolis_MTS_Agave_image_volume_grp_Stress_general_5.5.8", "JP_ID": "5bd3616943d9d339720e8ed3"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.5.8", "JP_ID": "5bd3616b43d9d339720e8ed9"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Webhooks_5.5.8", "JP_ID": "5bd3616b43d9d33953b43e58"}
    ],
    "NO-PC-HA": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_HA_Twonode_5.5.8", "JP_ID": "5bd3616b43d9d3385db970a3"}
    ],
    "GUEST-OS": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_5.5.8", "JP_ID": "5bd3616b43d9d339720e8ed7"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_api_stress_general_5.5.8", "JP_ID": "5bd3616c43d9d338aa730837"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Frodo_5.5.8", "JP_ID": "5bd3616a43d9d339720e8ed5"}
    ],
    "GPU": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.5.8", "JP_ID": "5bd3616a43d9d3387ce37a24"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_VGpu_5.5.8", "JP_ID": "5bd3616b43d9d3385db970a5"}
    ],
    "VNUMA": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Vnuma_5.5.8", "JP_ID": "5bd3616b43d9d32e90aaa2d5"}
    ]
}

UHURA_JPS_LTS_5_5_8 = {
    "NO-PC-WITH-VC": [
        {"JP_NAME": "Regression_Uhura__ESX__RPC_5.5.8", "JP_ID": "5bd3449243d9d31787e9ae1b"},
        {"JP_NAME": "Regression_Uhura__ESX__REST_5.5.8", "JP_ID": "5bd358b643d9d32e90aaa1a1"},
        {"JP_NAME": "Regression_Uhura__ESX__UI_5.5.8", "JP_ID": "5bd358b843d9d32d11582711"},
        {"JP_NAME": "Regression_Uhura__ManagementServer_5.5.8", "JP_ID": "5bd358b843d9d32e71c69268"}
    ],
    "NO-PC-NO-VC": [
        {"JP_NAME": "Regression_Uhura__AHV__REST_5.5.8", "JP_ID": "5bd358b543d9d32f1b11f5c8"},
        {"JP_NAME": "Regression_Uhura__AHV__RPC_5.5.8", "JP_ID": "5bd3449043d9d311988ad865"},
        {"JP_NAME": "Regression_Uhura__AHV__UI_5.5.8", "JP_ID": "5bd3449043d9d3155011c05e"}
    ],
    "NS-NO-VC": [
        {"JP_NAME": "Regression_Uhura__Ergon__NS_5.5.8", "JP_ID": "5bd358b843d9d32f6842fb75"}
    ]
}

ACROPOLIS_JPS_5_5_9 = {
    'GPU': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.5.9'),
                    ('JP_ID', u'5c555e3a7b48b1220ae9e740')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.5.9'),
                    ('JP_ID', u'5c555e3c7b48b1220ae9e743')])
    ],
    'GUEST-OS': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.5.9'),
                    ('JP_ID', u'5c555e207b48b1220ae9e717')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.5.9'),
                    ('JP_ID', u'5c555e237b48b1220ae9e71a')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.5.9'),
                    ('JP_ID', u'5c555e277b48b1220ae9e71e')])
    ],
    'NO-PC-HA': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.5.9'),
                     ('JP_ID', u'5c555e307b48b1220ae9e732')])
    ],
    'NO-PC': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.5.9'),
                    ('JP_ID', u'5c555e2a7b48b1220ae9e724')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.5.9'),
                    ('JP_ID', u'5c555e2c7b48b1220ae9e72e')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.5.9'),
                    ('JP_ID', u'5c555e2e7b48b1220ae9e730')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Agave_image_volume_grp_Stress_general_5.5.9'),
                    ('JP_ID', u'5c555e337b48b1220ae9e738')]),
#        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.5.9'), #Job Not supported for 5.5.x
#                    ('JP_ID', u'5c555e357b48b1220ae9e73a')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.5.9'),
                    ('JP_ID', u'5c555e387b48b1220ae9e73d')])
    ],
    'VNUMA': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.5.9'),
                    ('JP_ID', u'5c555e3e7b48b1220ae9e745')])
    ]
}

UHURA_JPS_LTS_5_5_9 = {
    'NO-PC-NO-VC': [
        OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.5.9'), ('JP_ID', u'5c57001a7b48b149b2ff00be')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.5.9'), ('JP_ID', u'5c57001c7b48b149b2ff00c1')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__UI_5.5.9'), ('JP_ID', u'5c57001f7b48b149b2ff00c4')])
    ],
    'NO-PC-WITH-VC': [
        OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.5.9'), ('JP_ID', u'5c5700107b48b149b2ff00ae')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.5.9'), ('JP_ID', u'5c5700137b48b149b2ff00b1')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.5.9'), ('JP_ID', u'5c5700157b48b149b2ff00b8')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.5.9'), ('JP_ID', u'5c5700177b48b149b2ff00bb')])
    ],
    'NS-NO-VC': [
        OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.5.9'), ('JP_ID', u'5c5700217b48b149b2ff00c9')])
    ],
    'NS-WITH-VC': [
        OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.5.9'), ('JP_ID', u'5c58179a7b48b1a1b7edad73')])
    ]
}

ACROPOLIS_JPS_5_10_2 = {
     "NO-PC": [
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.2", "JP_ID": "5c5120ad7b48b1be3eb222af"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.2", "JP_ID": "5c5120b77b48b1be3eb222c2"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.2", "JP_ID": "5c5120ba7b48b1be3eb222c5"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Ads_HA_5.10.2", "JP_ID": "5c5120a27b48b1be3eb2227c"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.10.2", "JP_ID": "5c5120b27b48b1be3eb222bb"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.10.2", "JP_ID": "5c5120b07b48b1be3eb222b2"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.2", "JP_ID": "5c51209e7b48b1be3eb22272"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Webhooks_5.10.2", "JP_ID": "5c5120997b48b1be3eb22269"}
     ],
     "NO-PC-HA": [
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.2", "JP_ID": "5c51209b7b48b1be3eb22270"}
     ],
     "GUEST-OS": [
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Guest_OS_5.10.2", "JP_ID": "5c5120937b48b1be3eb22253"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Frodo_5.10.2", "JP_ID": "5c5120b57b48b1be3eb222c0"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.2", "JP_ID": "5c5120967b48b1be3eb2225c"}
     ],
    "PC": [
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.2", "JP_ID": "5c51208e7b48b1be3eb22247"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.2", "JP_ID": "5c5120837b48b1be3eb22216"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.2", "JP_ID": "5c51208c7b48b1be3eb22238"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.2", "JP_ID": "5c5120877b48b1be3eb22220"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.2", "JP_ID": "5c5120817b48b1be3eb22209"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Metropolis_5.10.2", "JP_ID": "5c5120897b48b1be3eb22230"},
         {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Audit_5.10.2", "JP_ID": "5c5120917b48b1be3eb2224e"}
    ],
    "GPU": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.2", "JP_ID": "5c5120bf7b48b1be3eb222d1"},
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_VGpu_5.10.2", "JP_ID": "5c5120bc7b48b1be3eb222c8"}
    ],
    "VNUMA": [
        {"JP_NAME": "Regression_Acropolis_MTS_Nutest_Vnuma_5.10.2", "JP_ID": "5c5120c17b48b1be3eb222d5"}
    ]
}

UHURA_JPS_5_10_2 = {
    "PC": [
        {"JP_NAME": "Regression_Uhura_FEAT-6978_v3_clone_5.10.2", "JP_ID": "5c51628c7b48b17c366c94ad"},
        {"JP_NAME": "Regression_Uhura_GuestCustomization_5.10.2", "JP_ID": "5c5162937b48b17c366c94b7"},
        {"JP_NAME": "Regression_Uhura__PC__AHV__UI_5.10.2", "JP_ID": "5c51628e7b48b17c366c94b1"},
        {"JP_NAME": "Regression_Uhura__PC__UI_5.10.2", "JP_ID": "5c5162907b48b17c366c94b4"}
    ],
    "NO-PC-WITH-VC": [
        {"JP_NAME": "Regression_Uhura__ESX__RPC_5.10.2", "JP_ID": "5c51627e7b48b17c366c9495"},
        {"JP_NAME": "Regression_Uhura__ESX__REST_5.10.2", "JP_ID": "5c51627a7b48b17c366c948a"},
        {"JP_NAME": "Regression_Uhura__ESX__UI_5.10.2", "JP_ID": "5c5162837b48b17c366c949e"},
        {"JP_NAME": "Regression_Uhura__ManagementServer_5.10.2", "JP_ID": "5c5162807b48b17c366c949a"},
        {"JP_NAME": "Regression_Uhura_FEAT-3370_5.10.2", "JP_ID": "5c51627c7b48b17c366c948d"}
    ],
    "NO-PC-NO-VC": [
        {"JP_NAME": "Regression_Uhura__AHV__REST_5.10.2", "JP_ID": "5c5162857b48b17c366c94a1"},
        {"JP_NAME": "Regression_Uhura__AHV__RPC_5.10.2", "JP_ID": "5c5162877b48b17c366c94a4"},
        {"JP_NAME": "Regression_Uhura__AHV__UI_5.10.2", "JP_ID": "5c51628a7b48b17c366c94a7"}
    ],
    "NS-WITH-VC": [
        {"JP_NAME": "Regression_Uhura_GoldSuite_NS_5.10.2", "JP_ID": "5c5162957b48b17c366c94ba"}
    ],
    "NS-NO-VC": [
        {"JP_NAME": "Regression_Uhura__Ergon__NS_5.10.2", "JP_ID": "5c5162987b48b17c366c94be"}
    ]
}


UHURA_JPS_5_11 = {
    "PC": [
        {"JP_NAME": "Regression_Uhura_FEAT-6978_v3_clone_5.11", "JP_ID": "5c6fce457b48b19805b81e97", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura_GuestCustomization_5.11", "JP_ID": "5c6fce467b48b19805b81e99", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        #{"JP_NAME": "Regression_Uhura__PC__AHV__UI_5.11", "JP_ID": "5c6fce487b48b19805b81e9b", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        #{"JP_NAME": "Regression_Uhura__PC__UI_5.11", "JP_ID": "5c6fce4a7b48b19805b81e9d", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]}
    ],
    "NO-PC-WITH-VC": [
        {"JP_NAME": "Regression_Uhura__ESX__RPC_5.11", "JP_ID": "5c6fce367b48b19805b81e87", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__ESX__REST_5.11", "JP_ID": "5c6fce377b48b19805b81e89", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__ESX__UI_5.11", "JP_ID": "5c6fce397b48b19805b81e8b", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__ManagementServer_5.11", "JP_ID": "5c6fce3b7b48b19805b81e8d", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura_FEAT-3370_5.11", "JP_ID": "5c6fce3d7b48b19805b81e8f", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]}
    ],
    "NO-PC-NO-VC": [
        {"JP_NAME": "Regression_Uhura__AHV__REST_5.11", "JP_ID": "5c6fce3e7b48b19805b81e91", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__AHV__RPC_5.11", "JP_ID": "5c6fce417b48b19805b81e93", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]},
        {"JP_NAME": "Regression_Uhura__AHV__UI_5.11", "JP_ID": "5c6fce437b48b19805b81e95", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]}
    ],
    "NS-WITH-VC": [
        {"JP_NAME": "Regression_Uhura_GoldSuite_NS_5.11", "JP_ID": "5c6fce4b7b48b19805b81e9f", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]}
    ],
    "NS-NO-VC": [
        {"JP_NAME": "Regression_Uhura__Ergon__NS_5.11", "JP_ID": "5c6fce4d7b48b19805b81ea1", "FQA": ["velurusruthi.naidu@nutanix.com", "bhawani.singh@nutanix.com"]}
    ]
}

ACROPOLIS_JPS_5_11 = {
    'PC': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.11'), ('JP_ID', u'5c6fd64c7b48b19851451bb6'), ("FQA", ["bhawani.singh@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.11'), ('JP_ID', u'5c6fd64e7b48b19851451bb8'), ("FQA", ["bhawani.singh@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.11'), ('JP_ID', u'5cf4a8637b48b142dc5660d3'), ("FQA", ["saurabh.dohare@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.11'), ('JP_ID', u'5c6fd6527b48b19851451bbc'), ("FQA", ["saurabh.dohare@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.11'), ('JP_ID', u'5c6fd6547b48b19851451bbe'), ("FQA", ["bhawani.singh@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.11'), ('JP_ID', u'5c6fd6577b48b19851451bc0'), ("FQA", ["bhawani.singh@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.11'), ('JP_ID', u'5c6fd6597b48b19851451bc2'), ("FQA", ["bhawani.singh@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.11'), ('JP_ID', u'5c7778ce92491e33addfb6ba'), ("FQA", ["velurusruthi.naidu@nutanix.com"])])
    ],
    'GUEST-OS': [
#        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.11'), ('JP_ID', u'5c6fd6857b48b19851451bc4'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.11'), ('JP_ID', u'5c6fd6877b48b19851451bc6'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.11'), ('JP_ID', u'5c6fd6897b48b19851451bc8'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.11'), ('JP_ID', u'5c77792092491e33ac9d931c'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.11'), ('JP_ID', u'5c53d5037b48b1e0b12f3fd0'), ("FQA", ["velurusruthi.naidu@nutanix.com"])])
    ],
    'NO-PC': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.11'), ('JP_ID', u'5c6fd6a67b48b19805b8217b'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.11'), ('JP_ID', u'5c6fd6a87b48b19805b8217d'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.11'), ('JP_ID', u'5c6fd6aa7b48b19805b8217f'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.11'), ('JP_ID', u'5c6fd6ac7b48b19805b82181'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.11'), ('JP_ID', u'5c6fd6ae7b48b19805b82183'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.11'), ('JP_ID', u'5c6fd6b07b48b19805b82185'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.11'), ('JP_ID', u'5c6fd6b27b48b19805b82187'), ("FQA", ["bhawani.singh@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.11'), ('JP_ID', u'5c6fd6b47b48b19805b82189'), ("FQA", ["bhawani.singh@nutanix.com"])])
    ],
    'GPU': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_Single_Node_5.11'), ('JP_ID', u'5c6fd6fe7b48b19851451bcc'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_Three_Node_5.11'), ('JP_ID', u'5d133dcf7b48b1b4ec40fa13'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.11'), ('JP_ID', u'5c6fd7007b48b19851451bce'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.11'), ('JP_ID', u'5c750ec57b48b1525d1af7e5'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Gpu_Passthrough_Three_Node_5.11'), ('JP_ID', u'5d2da40e7b48b12ff69d7b09'), ("FQA", ["velurusruthi.naidu@nutanix.com"])])
    ],
    'NO-PC-HA': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.11'), ('JP_ID', u'5c6fd6fc7b48b19851451bca'), ("FQA", ["velurusruthi.naidu@nutanix.com"])])
    ],
    'VNUMA': [
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.11'), ('JP_ID', u'5c6fd7027b48b19851451bd0'), ("FQA", ["velurusruthi.naidu@nutanix.com"])]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.11'), ('JP_ID', u'5c7f91a27b48b1be9b2eede1'), ("FQA", ["velurusruthi.naidu@nutanix.com"])])
    ]
}

ACROPOLIS_JPS_5_11_1 ={
 #  'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_Single_Node_5.11.1'), ('JP_ID', u'5d53cafa7b48b1628f097b36')]),
 #         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_Three_Node_5.11.1'), ('JP_ID', u'5d53cafc7b48b1628f097b38')]),
 #         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.11.1'), ('JP_ID', u'5d53cafe7b48b1628f097b3a')]),
 #         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.11.1'), ('JP_ID', u'5d53cb007b48b1628f097b3c')]),
 #         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Gpu_Passthrough_Three_Node_5.11.1'), ('JP_ID', u'5d53cb017b48b1628f097b3e')])],
 # 'GUEST-OS': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.11.1'), ('JP_ID', u'5d52f48a7b48b1a5b7b5d44c')]),
 #              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.11.1'), ('JP_ID', u'5d53cb077b48b1628f097b44')]),
 #              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.11.1'), ('JP_ID', u'5d53cb097b48b1628f097b46')]),
 #              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.11.1'), ('JP_ID', u'5d53cb0b7b48b1628f097b48')]),
 #              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.11.1'), ('JP_ID', u'5d53cb0d7b48b1628f097b4a')])],
 # 'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.11.1'), ('JP_ID', u'5d53cac57b48b1fb7436df86')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.11.1'), ('JP_ID', u'5d53cac77b48b1fb7436df88')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.11.1'), ('JP_ID', u'5d53cac97b48b1fb7436df8a')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.11.1'), ('JP_ID', u'5d53caca7b48b1fb7436df8c')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.11.1'), ('JP_ID', u'5d53cacd7b48b1fb7436df8e')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.11.1'), ('JP_ID', u'5d53cace7b48b1fb7436df90')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.11.1'), ('JP_ID', u'5d53cad07b48b1fb7436df92')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.11.1'), ('JP_ID', u'5d53cad27b48b1fb7436df94')])],
 # 'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.11.1'), ('JP_ID', u'5d53cad47b48b1fb7436df96')])],
  'PC': [
 #        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.11.1'), ('JP_ID', u'5d53cad67b48b1fb7436df98')]),
 #        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.11.1'), ('JP_ID', u'5d53cad87b48b1fb7436df9a')]),
 #        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.11.1.x'), ('JP_ID', u'5d53cad97b48b1fb7436df9c')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.11.1'), ('JP_ID', u'5d53caf07b48b1628f097b2c')]),
 #        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.11.1'), ('JP_ID', u'5d53caf27b48b1628f097b2e')]),
 #        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.11.1'), ('JP_ID', u'5d53caf47b48b1628f097b30')]),
 #        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.11.1'), ('JP_ID', u'5d53caf77b48b1628f097b32')]),
 #        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.11.1'), ('JP_ID', u'5d53caf97b48b1628f097b34')])
],
 # 'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.11.1'), ('JP_ID', u'5d53cb037b48b1628f097b40')]),
 #           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.11.1'), ('JP_ID', u'5d53cb057b48b1628f097b42')])]
}



ACROPOLIS_JPS_5_10_3 = {
    'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.3'), ('JP_ID', u'5c7ccfe27b48b130c682c222')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.10.3'), ('JP_ID', u'5c7ccfe47b48b130c682c224')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.10.3'), ('JP_ID', u'5c7f92057b48b1ba51c49875')])
            ],
    'GUEST-OS': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.10.3'), ('JP_ID', u'5c7ccfc57b48b130c682c206')]),
                 OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.3'), ('JP_ID', u'5c7ccfc77b48b130c682c208')]),
                 OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.10.3'), ('JP_ID', u'5c7ccfca7b48b130c682c20a')]),
                 OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.10.3'), ('JP_ID', u'5c7ccfcb7b48b130c682c20c')])],
    'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.3'), ('JP_ID', u'5c7ccfce7b48b130c682c20e')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.3'), ('JP_ID', u'5c7ccfd07b48b130c682c210')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.3'), ('JP_ID', u'5c7ccfd37b48b130c682c212')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.10.3'), ('JP_ID', u'5c7ccfd57b48b130c682c214')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.10.3'), ('JP_ID', u'5c7ccfd77b48b130c682c216')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.10.3'), ('JP_ID', u'5c7ccfd97b48b130c682c218')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.3'), ('JP_ID', u'5c7ccfdb7b48b130c682c21a')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.10.3'), ('JP_ID', u'5c7ccfdd7b48b130c682c21c')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.10.3.'), ('JP_ID', u'5c7ccfde7b48b130c682c21e')])],
    'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.3'), ('JP_ID', u'5c7ccfe07b48b130c682c220')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.3'), ('JP_ID', u'5c7ccfb57b48b130c682c1f8')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.3'), ('JP_ID', u'5c7ccfb77b48b130c682c1fa')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.3'), ('JP_ID', u'5c7ccfb97b48b130c682c1fc')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.3'), ('JP_ID', u'5c7ccfbb7b48b130c682c1fe')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.3'), ('JP_ID', u'5c7ccfbe7b48b130c682c200')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.10.3'), ('JP_ID', u'5c7ccfc07b48b130c682c202')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.10.3'), ('JP_ID', u'5c7ccfc27b48b130c682c204')])],
    'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.10.3'), ('JP_ID', u'5c7ccfe67b48b130c682c226')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.10.3'), ('JP_ID', u'5c7f914d7b48b1ba51c49873')])]
}


ACROPOLIS_JPS_5_10_3_2 = {
    'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.3.2'), ('JP_ID', u'5cac46627b48b18febf8ff2a')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.10.3.2'), ('JP_ID', u'5cac46647b48b18febf8ff2c')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.10.3.2'), ('JP_ID', u'5cac46657b48b18febf8ff2e')])],
    'GUEST-OS': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.10.3.2'), ('JP_ID', u'5cac46477b48b18febf8ff0d')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.3.2'), ('JP_ID', u'5cac46497b48b18febf8ff0f')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.10.3.2'), ('JP_ID', u'5cac464b7b48b18febf8ff11')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.10.3.2'), ('JP_ID', u'5cac464d7b48b18febf8ff13')])],
    'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.3.2'), ('JP_ID', u'5cac464f7b48b18febf8ff15')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.3.2'), ('JP_ID', u'5cac46517b48b18febf8ff17')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.3.2'), ('JP_ID', u'5cac46527b48b18febf8ff19')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.10.3.2'), ('JP_ID', u'5cac46547b48b18febf8ff1b')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.10.3.2'), ('JP_ID', u'5cac46567b48b18febf8ff1e')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.10.3.2'), ('JP_ID', u'5cac46587b48b18febf8ff20')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.3.2'), ('JP_ID', u'5cac465a7b48b18febf8ff22')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.10.3.2'), ('JP_ID', u'5cac465c7b48b18febf8ff24')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.10.3.2.'), ('JP_ID', u'5cac465e7b48b18febf8ff26')])],
    'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.3.2'), ('JP_ID', u'5cac46607b48b18febf8ff28')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.3.2'), ('JP_ID', u'5cac46397b48b18febf8feff')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.3.2'), ('JP_ID', u'5cac463b7b48b18febf8ff01')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.3.2'), ('JP_ID', u'5cac463d7b48b18febf8ff03')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.3.2'), ('JP_ID', u'5cac463f7b48b18febf8ff05')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.3.2'), ('JP_ID', u'5cac46417b48b18febf8ff07')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.10.3.2'), ('JP_ID', u'5cac46437b48b18febf8ff09')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.10.3.2'), ('JP_ID', u'5cac46457b48b18febf8ff0b')])],
    'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.10.3.2'), ('JP_ID', u'5cac46677b48b18febf8ff30')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.10.3.2'), ('JP_ID', u'5cac46697b48b18febf8ff32')])]
}

UHURA_JPS_5_10_3 = {
    'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.10.3'), ('JP_ID', u'5c7cd1a47b48b130c575d009')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.10.3'), ('JP_ID', u'5c7cd1a67b48b130c575d00b')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__UI_5.10.3'), ('JP_ID', u'5c7cd1a87b48b130c575d00d')])],
    'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.10.3'), ('JP_ID', u'5c7cd1977b48b130c575cfff')]),
                      OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.10.3'), ('JP_ID', u'5c7cd19a7b48b130c575d001')]),
                      OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.10.3'), ('JP_ID', u'5c7cd19c7b48b130c575d003')]),
                      OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.10.3'), ('JP_ID', u'5c7cd19f7b48b130c575d005')]),
                      OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.10.3'), ('JP_ID', u'5c7cd1a17b48b130c575d007')])],
    'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.10.3'), ('JP_ID', u'5c7cd1b67b48b130c575d019')])],
    'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.10.3'), ('JP_ID', u'5c7cd1b37b48b130c575d017')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.10.3'), ('JP_ID', u'5c7cd1aa7b48b130c575d00f')]),
           OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.10.3'), ('JP_ID', u'5c7cd1ac7b48b130c575d011')]),
           OrderedDict([('JP_NAME', u'Regression_Uhura__PC__AHV__UI_5.10.3'), ('JP_ID', u'5c7cd1af7b48b130c575d013')]),
           OrderedDict([('JP_NAME', u'Regression_Uhura__PC__UI_5.10.3'), ('JP_ID', u'5c7cd1b17b48b130c575d015')])]
}


UHURA_JPS_5_10_3_2 = {
    'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.10.3.2'), ('JP_ID', u'5cac48487b48b18febf8ff57')]),
                 OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.10.3.2'), ('JP_ID', u'5cac484a7b48b18febf8ff59')]),
                 OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__UI_5.10.3.2'), ('JP_ID', u'5cac484c7b48b18febf8ff5b')])],
    'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.10.3.2'), ('JP_ID', u'5cac483e7b48b18febf8ff4d')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.10.3.2'), ('JP_ID', u'5cac48407b48b18febf8ff4f')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.10.3.2'), ('JP_ID', u'5cac48427b48b18febf8ff51')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.10.3.2'), ('JP_ID', u'5cac48447b48b18febf8ff53')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.10.3.2'), ('JP_ID', u'5cac48467b48b18febf8ff55')])],
    'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.10.3.2'), ('JP_ID', u'5cac48587b48b18febf8ff67')])],
    'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.10.3.2'), ('JP_ID', u'5cac48567b48b18febf8ff65')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.10.3.2'), ('JP_ID', u'5cac484e7b48b18febf8ff5d')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.10.3.2'), ('JP_ID', u'5cac48507b48b18febf8ff5f')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__PC__AHV__UI_5.10.3.2'), ('JP_ID', u'5cac48527b48b18febf8ff61')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__PC__UI_5.10.3.2'), ('JP_ID', u'5cac48547b48b18febf8ff63')])]
}

ACROPOLIS_JPS_5_10_4 ={
    'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.4'), ('JP_ID', u'5cbeb45b7b48b124bb8592c2')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.10.4'), ('JP_ID', u'5cbeb45d7b48b124bb8592c4')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.10.4'), ('JP_ID', u'5cbeb45f7b48b124bb8592c6')])],
    'GUEST-OS': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.10.4'), ('JP_ID', u'5cbeb43f7b48b124bb85921f')]),
                 OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.4'), ('JP_ID', u'5cbeb4417b48b124bb859221')]),
                 OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.10.4'), ('JP_ID', u'5cbeb4437b48b124bb859223')]),
                 OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.10.4'), ('JP_ID', u'5cbeb4457b48b124bb859226')])],
    'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.4'), ('JP_ID', u'5cbeb4477b48b124bb8592ae')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.4'), ('JP_ID', u'5cbeb4497b48b124bb8592b0')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.4'), ('JP_ID', u'5cbeb44b7b48b124bb8592b2')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.10.4'), ('JP_ID', u'5cbeb44d7b48b124bb8592b4')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.10.4'), ('JP_ID', u'5cbeb44f7b48b124bb8592b6')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.10.4'), ('JP_ID', u'5cbeb4517b48b124bb8592b8')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.4'), ('JP_ID', u'5cbeb4537b48b124bb8592ba')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.10.4'), ('JP_ID', u'5cbeb4557b48b124bb8592bc')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.10.4'), ('JP_ID', u'5cbeb4577b48b124bb8592be')])],
    'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.4'), ('JP_ID', u'5cbeb4597b48b124bb8592c0')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.4'), ('JP_ID', u'5cbeb42f7b48b124bb859210')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.4'), ('JP_ID', u'5cbeb4317b48b124bb859212')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.4'), ('JP_ID', u'5cbeb4337b48b124bb859214')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.4'), ('JP_ID', u'5cbeb4367b48b124bb859217')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.4'), ('JP_ID', u'5cbeb4387b48b124bb859219')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.10.4'), ('JP_ID', u'5cbeb43a7b48b124bb85921b')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.10.4'), ('JP_ID', u'5cbeb43c7b48b124bb85921d')])],
    'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.10.4'), ('JP_ID', u'5cbeb4617b48b124bb8592c8')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.10.4'), ('JP_ID', u'5cbeb4637b48b124bb8592ca')])]
}

UHURA_JPS_5_10_4 = {
    'NO-PC-NO-VC': [
                OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.10.4'), ('JP_ID', u'5cbf52c67b48b142bcd727c6')]),
                OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.10.4'), ('JP_ID', u'5cbf52c87b48b142bcd727c8')]),
                OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__UI_5.10.4'), ('JP_ID', u'5cbf52ca7b48b142bcd727ca')])
    ],
    'NO-PC-WITH-VC': [
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.10.4'), ('JP_ID', u'5cbf52bb7b48b142bcd727bc')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.10.4'), ('JP_ID', u'5cbf52bd7b48b142bcd727be')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.10.4'), ('JP_ID', u'5cbf52bf7b48b142bcd727c0')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.10.4'), ('JP_ID', u'5cbf52c17b48b142bcd727c2')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.10.4'), ('JP_ID', u'5cbf52c47b48b142bcd727c4')])
    ],
    'NS-NO-VC': [
                OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.10.4'), ('JP_ID', u'5cbf52d97b48b142bcd727d6')])
    ],
    'NS-WITH-VC': [
                OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.10.4'), ('JP_ID', u'5cbf52d57b48b142bcd727d4')])
    ],
    'PC': [
        OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.10.4'), ('JP_ID', u'5cbf52cd7b48b142bcd727cc')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.10.4'), ('JP_ID', u'5cbf52cf7b48b142bcd727ce')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__PC__AHV__UI_5.10.4'), ('JP_ID', u'5cbf52d17b48b142bcd727d0')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura__PC__UI_5.10.4'), ('JP_ID', u'5cbf52d37b48b142bcd727d2')])
    ]
}

ACROPOLIS_JPS_5_10_5 = {
    'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.5'), ('JP_ID', u'5ce23d227b48b15090ba16f7')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.10.5'), ('JP_ID', u'5ce23d247b48b15090ba16f9')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.10.5'), ('JP_ID', u'5ce23d267b48b15090ba16fb')])],
    'GUEST-OS': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.10.5'), ('JP_ID', u'5ce23d017b48b15090ba16d9')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.5'), ('JP_ID', u'5ce23d037b48b15090ba16db')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.10.5'), ('JP_ID', u'5ce23d057b48b15090ba16dd')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.10.5'), ('JP_ID', u'5ce23d087b48b15090ba16df')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.10.5'), ('JP_ID', u'5ce23d0a7b48b15090ba16e1')])],
    'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.5'), ('JP_ID', u'5ce23d0c7b48b15090ba16e3')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.5'), ('JP_ID', u'5ce23d0e7b48b15090ba16e5')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.5'), ('JP_ID', u'5ce23d117b48b15090ba16e7')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.10.5'), ('JP_ID', u'5ce23d137b48b15090ba16e9')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.10.5'), ('JP_ID', u'5ce23d157b48b15090ba16eb')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.10.5'), ('JP_ID', u'5ce23d177b48b15090ba16ed')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.5'), ('JP_ID', u'5ce23d197b48b15090ba16ef')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.10.5'), ('JP_ID', u'5ce23d1b7b48b15090ba16f1')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.10.5'), ('JP_ID', u'5ce23d1d7b48b15090ba16f3')])],
    'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.5'), ('JP_ID', u'5ce23d1f7b48b15090ba16f5')])],
    'PC': [#OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_OVA_AHV_AHV_5.10.5'), ('JP_ID', u'5ce23cf07b48b15090ba16c9')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.5'), ('JP_ID', u'5ce23cf27b48b15090ba16cb')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.5'), ('JP_ID', u'5ce23cf57b48b15090ba16cd')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.5'), ('JP_ID', u'5ce23cf77b48b15090ba16cf')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.5'), ('JP_ID', u'5ce23cf97b48b15090ba16d1')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.5'), ('JP_ID', u'5ce23cfb7b48b15090ba16d3')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.10.5'), ('JP_ID', u'5ce23cfd7b48b15090ba16d5')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.10.5'), ('JP_ID', u'5ce23cff7b48b15090ba16d7')])],
    'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.10.5'), ('JP_ID', u'5ce23d287b48b15090ba16fd')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.10.5'), ('JP_ID', u'5ce23d2b7b48b15090ba16ff')])]
}

UHURA_JPS_5_10_5 = {
    'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.10.5'), ('JP_ID', u'5ce69f4c7b48b152abeafddd')]),
                 OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.10.5'), ('JP_ID', u'5ce69f4e7b48b152abeafddf')])],
  'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.10.5'), ('JP_ID', u'5ce69f2d7b48b1f941a458bc')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.10.5'), ('JP_ID', u'5ce69f2f7b48b1f941a458be')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.10.5'), ('JP_ID', u'5ce69f467b48b152abeafdd7')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.10.5'), ('JP_ID', u'5ce69f487b48b152abeafdd9')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.10.5'), ('JP_ID', u'5ce69f4a7b48b152abeafddb')])],
  'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.10.5'), ('JP_ID', u'5ce69f557b48b152abeafde7')])],
  'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.10.5'), ('JP_ID', u'5ce69f537b48b152abeafde5')])],
  'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.10.5'), ('JP_ID', u'5ce69f507b48b152abeafde1')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.10.5'), ('JP_ID', u'5ce69f517b48b152abeafde3')])]
}

ACROPOLIS_JPS_5_10_6 = {
    'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.6'), ('JP_ID', u'5d1313737b48b1115c517950')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.10.6'), ('JP_ID', u'5d1313757b48b1115c517952')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.10.6'), ('JP_ID', u'5d1313777b48b1115c517954')])],
    'GUEST-OS': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.10.6'), ('JP_ID', u'5d13137e7b48b1115c51795a')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.6'), ('JP_ID', u'5d1313807b48b1115c51795c')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.10.6'), ('JP_ID', u'5d1313827b48b1115c51795e')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.10.6'), ('JP_ID', u'5d1313847b48b1115c517960')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.10.6'), ('JP_ID', u'5d1313867b48b1115c517962')])],
    'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.6'), ('JP_ID', u'5d13133b7b48b1320fead868')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.6'), ('JP_ID', u'5d13133e7b48b1320fead86a')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.6'), ('JP_ID', u'5d1313547b48b1115c517932')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.10.6'), ('JP_ID', u'5d1313577b48b1115c517934')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.10.6'), ('JP_ID', u'5d1313597b48b1115c517936')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.10.6'), ('JP_ID', u'5d13135b7b48b1115c517938')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.6'), ('JP_ID', u'5d13135d7b48b1115c51793a')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.10.6'), ('JP_ID', u'5d13135f7b48b1115c51793c')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.10.6'), ('JP_ID', u'5d1313617b48b1115c51793e')])],
    'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.6'), ('JP_ID', u'5d1313637b48b1115c517940')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.6'), ('JP_ID', u'5d1313647b48b1115c517942')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.6'), ('JP_ID', u'5d1313667b48b1115c517944')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.6'), ('JP_ID', u'5d1313697b48b1115c517946')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.6'), ('JP_ID', u'5d13136b7b48b1115c517948')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.6'), ('JP_ID', u'5d13136d7b48b1115c51794a')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.10.6'), ('JP_ID', u'5d13136f7b48b1115c51794c')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.10.6'), ('JP_ID', u'5d1313717b48b1115c51794e')])],
  'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.10.6'), ('JP_ID', u'5d1313797b48b1115c517956')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.10.6'), ('JP_ID', u'5d13137b7b48b1115c517958')])]
}

ACROPOLIS_JPS_5_12 = {
    'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.12'), ('JP_ID', u'5d400e3f7b48b19cdebd8c05')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.12'), ('JP_ID', u'5d400e407b48b19cdebd8c07')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.12'), ('JP_ID', u'5d400e427b48b19cdebd8c09')])],
    'GUEST-OS': [#OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.12'), ('JP_ID', u'5d400e227b48b19cdebd8be7')]),
                OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.12'), ('JP_ID', u'5d400e247b48b19cdebd8be9')]),
                OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.12'), ('JP_ID', u'5d400e267b48b19cdebd8beb')]),
                OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.12'), ('JP_ID', u'5d400e287b48b19cdebd8bed')]),
                 OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.12'), ('JP_ID', u'5d400e2b7b48b19cdebd8bef')])],
    'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.12'), ('JP_ID', u'5d400e2d7b48b19cdebd8bf1')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.12'), ('JP_ID', u'5d400e2e7b48b19cdebd8bf3')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.12'), ('JP_ID', u'5d400e307b48b19cdebd8bf5')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.12'), ('JP_ID', u'5d400e327b48b19cdebd8bf7')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.12'), ('JP_ID', u'5d400e347b48b19cdebd8bf9')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.12'), ('JP_ID', u'5d400e367b48b19cdebd8bfb')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.12'), ('JP_ID', u'5d400e377b48b19cdebd8bfd')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.12'), ('JP_ID', u'5d400e397b48b19cdebd8bff')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.12'), ('JP_ID', u'5d400e3b7b48b19cdebd8c01')])],
    'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.12'), ('JP_ID', u'5d400e3d7b48b19cdebd8c03')])],
    'PC': [#OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_OVA_AHV_AHV_5.12'), ('JP_ID', u'5d400e157b48b19cdebd8bd7')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.12'), ('JP_ID', u'5d400e167b48b19cdebd8bd9')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.12'), ('JP_ID', u'5d400e187b48b19cdebd8bdb')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.12'), ('JP_ID', u'5d400e1a7b48b19cdebd8bdd')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.12'), ('JP_ID', u'5d400e1b7b48b19cdebd8bdf')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.12'), ('JP_ID', u'5d400e1d7b48b19cdebd8be1')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.12'), ('JP_ID', u'5d400e1f7b48b19cdebd8be3')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.12'), ('JP_ID', u'5d400e217b48b19cdebd8be5')])],
    'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.12'), ('JP_ID', u'5d400e457b48b19cdebd8c0b')]),
            OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.12'), ('JP_ID', u'5d400e477b48b19cdebd8c0d')])]
}


UHURA_JPS_5_12 = {
    'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.12'), ('JP_ID', u'5d4011f67b48b198ad555ff6')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.12'), ('JP_ID', u'5d4011f87b48b198ad555ff8')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__UI_5.12'), ('JP_ID', u'5d4011f97b48b198ad555ffa')])],
    'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.12'), ('JP_ID', u'5d4011ec7b48b198ad555fec')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.12'), ('JP_ID', u'5d4011ef7b48b198ad555fee')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.12'), ('JP_ID', u'5d4011f07b48b198ad555ff0')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.12'), ('JP_ID', u'5d4011f27b48b198ad555ff2')]),
                    OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.12'), ('JP_ID', u'5d4011f47b48b198ad555ff4')])],
    'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.12'), ('JP_ID', u'5d4012017b48b198ad556002')])],
    'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.12'), ('JP_ID', u'5d4011ff7b48b198ad556000')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.12'), ('JP_ID', u'5d4011fb7b48b198ad555ffc')]),
            OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.12'), ('JP_ID', u'5d4011fd7b48b198ad555ffe')])]
}


UHURA_JPS_5_10_6 = {
    'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.10.6'), ('JP_ID', u'5d17098e7b48b1285aa9eb97')]),
                 OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.10.6'), ('JP_ID', u'5d17098f7b48b1285aa9eb99')])],
 'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.10.6'), ('JP_ID', u'5d1709837b48b1285aa9eb8d')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.10.6'), ('JP_ID', u'5d1709857b48b1285aa9eb8f')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.10.6'), ('JP_ID', u'5d1709887b48b1285aa9eb91')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.10.6'), ('JP_ID', u'5d17098a7b48b1285aa9eb93')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.10.6'), ('JP_ID', u'5d17098c7b48b1285aa9eb95')])],
 'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.10.6'), ('JP_ID', u'5d1709977b48b1285aa9eba3')])],
 'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.10.6'), ('JP_ID', u'5d1709957b48b1285aa9eb9f')])],
 'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.10.6'), ('JP_ID', u'5d1709917b48b1285aa9eb9b')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.10.6'), ('JP_ID', u'5d1709937b48b1285aa9eb9d')])]
}


UHURA_JPS_5_10_7 = {'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.10.7'), ('JP_ID', u'5d4d13717b48b16cb671b66c')]),
                 OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.10.7'), ('JP_ID', u'5d4d13747b48b16cb671b66e')])],
 'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.10.7'), ('JP_ID', u'5d4d13667b48b16cb671b662')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.10.7'), ('JP_ID', u'5d4d13687b48b16cb671b664')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.10.7'), ('JP_ID', u'5d4d136a7b48b16cb671b666')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.10.7'), ('JP_ID', u'5d4d136c7b48b16cb671b668')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.10.7'), ('JP_ID', u'5d4d13707b48b16cb671b66a')])],
 'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.10.7'), ('JP_ID', u'5d4d137c7b48b16cb671b676')])],
 'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.10.7'), ('JP_ID', u'5d4d137a7b48b16cb671b674')])],
 'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.10.7'), ('JP_ID', u'5d4d13767b48b16cb671b670')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.10.7'), ('JP_ID', u'5d4d13787b48b16cb671b672')])]
}

ACROPOLIS_JPS_5_10_7 = {
    'GPU': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.7'), ('JP_ID', u'5d4d121e7b48b17e0bc2bd8a')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.10.7'), ('JP_ID', u'5d4d12217b48b17e0bc2bd8c')]),
         OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.10.7'), ('JP_ID', u'5d4d12237b48b17e0bc2bd8e')])],
    'GUEST-OS': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_5.10.7'), ('JP_ID', u'5d4d12297b48b17e0bc2bd94')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.7'), ('JP_ID', u'5d4d122b7b48b17e0bc2bd96')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.10.7'), ('JP_ID', u'5d4d122e7b48b17e0bc2bd98')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.10.7'), ('JP_ID', u'5d4d12307b48b17e0bc2bd9a')]),
              OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.10.7'), ('JP_ID', u'5d4d12327b48b17e0bc2bd9c')])],
    'NO-PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.7'), ('JP_ID', u'5d4d11f97b48b17e0bc2bd67')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.7'), ('JP_ID', u'5d4d11fb7b48b17e0bc2bd69')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.7'), ('JP_ID', u'5d4d11fd7b48b17e0bc2bd6b')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_HA_5.10.7'), ('JP_ID', u'5d4d11ff7b48b17e0bc2bd6d')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_5.10.7'), ('JP_ID', u'5d4d12017b48b17e0bc2bd6f')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_5.10.7'), ('JP_ID', u'5d4d12037b48b17e0bc2bd71')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.7'), ('JP_ID', u'5d4d12067b48b17e0bc2bd73')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.10.7'), ('JP_ID', u'5d4d12087b48b17e0bc2bd75')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.10.7'), ('JP_ID', u'5d4d120b7b48b17e0bc2bd77')])],
    'NO-PC-HA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.7'), ('JP_ID', u'5d4d120d7b48b17e0bc2bd79')])],
    'PC': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.7'), ('JP_ID', u'5d4d120f7b48b17e0bc2bd7b')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.7'), ('JP_ID', u'5d4d12117b48b17e0bc2bd7e')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.7'), ('JP_ID', u'5d4d12137b48b17e0bc2bd80')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.7'), ('JP_ID', u'5d4d12157b48b17e0bc2bd82')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.7'), ('JP_ID', u'5d4d12177b48b17e0bc2bd84')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.10.7'), ('JP_ID', u'5d4d12197b48b17e0bc2bd86')]),
        OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.10.7'), ('JP_ID', u'5d4d121c7b48b17e0bc2bd88')])],
    'VNUMA': [OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.10.7'), ('JP_ID', u'5d4d12257b48b17e0bc2bd90')]),
           OrderedDict([('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.10.7'), ('JP_ID', u'5d4d12277b48b17e0bc2bd92')])]
}


UHURA_JPS_5_11_1 ={
    'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.11.1'), ('JP_ID', u'5d5651a37b48b10192be6028')]),
                 OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.11.1'), ('JP_ID', u'5d5651a57b48b10192be602a')]),
                 OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__UI_5.11.1'), ('JP_ID', u'5d5651a87b48b10192be602c')])],
 'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.11.1'), ('JP_ID', u'5d5651977b48b10192be601e')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.11.1'), ('JP_ID', u'5d5651997b48b10192be6020')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.11.1'), ('JP_ID', u'5d56519b7b48b10192be6022')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.11.1'), ('JP_ID', u'5d56519e7b48b10192be6024')]),
                   OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.11.1'), ('JP_ID', u'5d5651a07b48b10192be6026')])],
 'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.11.1'), ('JP_ID', u'5d5651b27b48b10192be6034')])],
 'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.11.1'), ('JP_ID', u'5d5651b07b48b10192be6032')])],
 'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.11.1'), ('JP_ID', u'5d5651ab7b48b10192be602e')]),
        OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.11.1'), ('JP_ID', u'5d5651ad7b48b10192be6030')])]
}


ACROPOLIS_JPS_5_10_9 = {
    'GPU': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.10.9'), ('sub-component', 'gpu'), ('JP_ID', u'5db7d76b7b48b12296552fc7'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.10.9'), ('sub-component', 'gpu'), ('JP_ID', u'5db7d76d7b48b12296552fc9'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.10.9'), ('sub-component', 'gpu'), ('JP_ID', u'5db7d76f7b48b12296552fcb'), ('max_dep', [u'max_deployments__1'])])],
    'GUEST-OS-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_1_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7817b48b12296552fdd'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_2_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7847b48b12296552fdf'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_3_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7877b48b12296552fe1'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_4_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7897b48b12296552fe3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_5_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d78b7b48b12296552fe5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_6_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d78e7b48b12296552fe7'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_1_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7907b48b12296552fe9'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_2_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7927b48b12296552feb'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_1_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7957b48b12296552fed'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_2_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7977b48b12296552fef'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_1_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7997b48b12296552ff1'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_2_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d79b7b48b12296552ff3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_3_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d79e7b48b12296552ff5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_1_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7a07b48b12296552ff7'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_2_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7a27b48b12296552ff9'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_3_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7a57b48b12296552ffb'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_4_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7a77b48b12296552ffd'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_5_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7ab7b48b1229521f1bf'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_6_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7ad7b48b1229521f1c1'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_7_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7b07b48b1229521f1c3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_1_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7b27b48b1229521f1c5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_2_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7b57b48b1229521f222'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_1_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7b77b48b1229521f224'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_2_5.10.9'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5db7d7b97b48b1229521f226'), ('max_dep', [u'max_deployments__1'])])],
    'GUEST-OS-OTHERS': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.10.9'), ('sub-component', 'api-stress'), ('JP_ID', u'5db7d7477b48b12296552faa'), ('max_dep', [u'max_deployments__1'])]),
                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.10.9'), ('sub-component', 'frodo'), ('JP_ID', u'5db7d74a7b48b12296552fac'), ('max_dep', [u'max_deployments__5'])]),
                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.10.9'), ('sub-component', 'ahv-co'), ('JP_ID', u'5db7d74d7b48b12296552fae'), ('max_dep', [u'max_deployments__3'])]),
                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.9'), ('sub-component', 'ahv-ns'), ('JP_ID', u'5db7d7577b48b12296552fb6'), ('max_dep', [u'max_deployments__1'])]),
                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.10.9'), ('sub-component', 'vnuma'), ('JP_ID', u'5db7d7737b48b12296552fcf'), ('max_dep', [u'max_deployments__1'])]),
                    #OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.10.9'), ('sub-component', 'host-agent'), ('JP_ID', u'5db7d7507b48b12296552fb0'), ('max_dep', [u'max_deployments__1'])])
                    ],
    'NO-PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.10.9'), ('sub-component', 'aos-ns'), ('JP_ID', u'5db7d7557b48b12296552fb4'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.10.9'), ('sub-component', 'ahv-ns'), ('JP_ID', u'5db7d7577b48b12296552fb6'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.10.9'), ('sub-component', 'vm-management'), ('JP_ID', u'5db7d75a7b48b12296552fb8'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.10.9'), ('sub-component', 'v3-vm-management'), ('JP_ID', u'5db7d75c7b48b12296552fba'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.10.9'), ('sub-component', 'webhooks'), ('JP_ID', u'5db7d75e7b48b12296552fbc'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.10.9'), ('sub-component', 'ahv-co'), ('JP_ID', u'5db7d7617b48b12296552fbe'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_ACLI_Scheduling_5.10.9'), ('sub-component', 'scheduler-acli'), ('JP_ID', u'5db7d7637b48b12296552fc0'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Storage_Persona_5.10.9'), ('sub-component', 'storage-persona'), ('JP_ID', u'5db7d7667b48b12296552fc2'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_Defrag_5.10.9'), ('sub-component', 'storage-persona'), ('JP_ID', u'5db7d7687b48b12296552fc4'), ('max_dep', [u'max_deployments__1'])])],
    'NO-PC-HA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7527b48b12296552fb2'), ('max_dep', [u'max_deployments__1'])])],
    'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.10.9'), ('sub-component', 'batch-vms'), ('JP_ID', u'5db7d73c7b48b12296552fa0'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.10.9'), ('sub-component', 'batch-vms'), ('JP_ID', u'5db7d73e7b48b12296552fa2'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.10.9'), ('sub-component', 'metropolis'), ('JP_ID', u'5db7d7407b48b12296552fa4'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.10.9'), ('sub-component', 'metropolis'), ('JP_ID', u'5db7d7437b48b12296552fa6'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.10.9'), ('sub-component', 'audit'), ('JP_ID', u'5db7d7457b48b12296552fa8'), ('max_dep', [u'max_deployments__1'])])],
    'PC-CATALOG': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.10.9'), ('sub-component', 'catalog'), ('JP_ID', u'5db7d7337b48b12296552f98'), ('max_dep', [u'max_deployments__1'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_5.10.9'), ('sub-component', 'catalog'), ('JP_ID', u'5db7d7357b48b12296552f9a'), ('max_dep', [u'max_deployments__3'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_5.10.9'), ('sub-component', 'catalog'), ('JP_ID', u'5db7d7377b48b12296552f9c'), ('max_dep', [u'max_deployments__2'])])],
    'PC-CATALOG-HYPERVISOR-ANY': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.10.9'), ('sub-component', 'catalog'), ('JP_ID', u'5db7d73a7b48b12296552f9e'), ('max_dep', [u'max_deployments__6'])])],
    'SCHEDULER-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_1_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7bb7b48b1229521f228'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_2_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7be7b48b1229521f22a'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_3_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7c07b48b1229521f22c'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_1_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7c37b48b1229521f22e'), ('max_dep', [u'max_deployments__10'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_2_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7c57b48b1229521f230'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_3_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7c77b48b1229521f232'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_1_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7ca7b48b1229521f234'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_2_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7cc7b48b1229521f236'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_Set_1_5.10.9'), ('sub-component', 'scheduler'), ('JP_ID', u'5db7d7cf7b48b1229521f238'), ('max_dep', [u'max_deployments__2'])])],
    'VNUMA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.10.9'), ('sub-component', 'vnuma'), ('JP_ID', u'5db7d7717b48b12296552fcd'), ('max_dep', [u'max_deployments__1'])])],
    'Xi-MGMT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6906_5.10.9'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5db7d7767b48b12296552fd1'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Xi_Telemetry_FEAT_4361_5.10.9'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5db7d7787b48b12296552fd3'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6626_5.10.9'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5db7d77b7b48b12296552fd5'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_API_5.10.9'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5db7d77d7b48b12296552fd7'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_OP-xi_API_5.10.9'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5db7d77f7b48b12296552fd9'), ('max_dep', [u'max_deployments__1'])])]
}



UHURA_JPS_5_10_9 = {
    'NO-PC-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__REST_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d717b48b1f02202a692'), ('max_dep', [u'max_deployments__1'])]),
                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__RPC_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d737b48b1f02202a694'), ('max_dep', [u'max_deployments__2'])]),
                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__UI_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d767b48b1f02202a696'), ('max_dep', [u'max_deployments__1'])])],
    'NO-PC-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__RPC_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d637b48b1f02202a687'), ('max_dep', [u'max_deployments__3'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__REST_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d667b48b1f02202a68a'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__UI_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d697b48b1f02202a68c'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ManagementServer_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d6b7b48b1f02202a68e'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-3370_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d6e7b48b1f02202a690'), ('max_dep', [u'max_deployments__1'])])],
    'NS-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__Ergon__NS_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d807b48b1f02202a69e'), ('max_dep', [u'max_deployments__1'])])],
    'NS-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d7d7b48b1f02202a69c'), ('max_dep', [u'max_deployments__1'])])],
    'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d787b48b1f02202a698'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GuestCustomization_5.10.9'), ('sub-component', 'uhura'), ('JP_ID', u'5db68d7b7b48b1f02202a69a'), ('max_dep', [u'max_deployments__3'])])]
}


ACROPOLIS_JPS_5_16 ={
    'GPU': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.16'), ('sub-component', 'gpu'), ('JP_ID', u'5dbff3e97b48b12e7aaf5eab'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.16'), ('sub-component', 'gpu'), ('JP_ID', u'5dbff3ea7b48b12e7aaf5ead'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.16'), ('sub-component', 'gpu'), ('JP_ID', u'5dbff3fb7b48b12e7aaf5eaf'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_1_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4097b48b12e7aaf5ebf'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_2_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff40b7b48b12e7aaf5ec1'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_3_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff40d7b48b12e7aaf5ec3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_4_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4257b48b131b2c656c5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_5_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4277b48b131b2c656c7'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_6_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4297b48b131b2c656c9'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_1_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff42a7b48b131b2c656cb'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_2_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff42d7b48b134e56ef9b3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_1_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff42f7b48b134e56ef9b5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_2_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4317b48b134e56ef9b7'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_1_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4327b48b134e56ef9b9'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_2_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4347b48b134e56ef9bb'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_3_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4367b48b134e56ef9bd'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_1_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4387b48b134e56ef9bf'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_2_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4397b48b134e56ef9c1'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_3_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff43b7b48b134e56ef9c3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_4_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff43d7b48b134e56ef9c5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_5_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff43f7b48b134e56ef9c7'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_6_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4407b48b134e56ef9c9'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_7_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4427b48b134e56ef9cf'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_1_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4447b48b134e56ef9d1'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_2_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4467b48b134e56ef9d3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_1_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4477b48b134e56ef9d5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_2_5.16'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dbff4497b48b134e56ef9d7'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OTHERS': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.16'), ('sub-component', 'api-stress'), ('JP_ID', u'5dbff3ce7b48b12e7aaf5e8e'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.16'), ('sub-component', 'frodo'), ('JP_ID', u'5dbff3d27b48b12e7aaf5e90'), ('max_dep', [u'max_deployments__5'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.16'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dbff3d47b48b12e7aaf5e92'), ('max_dep', [u'max_deployments__3'])]),
                    OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.16'), ('sub-component', 'ahv-ns'), ('JP_ID', u'5dbff3db7b48b12e7aaf5e9a'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.16'), ('sub-component', 'host-agent'), ('JP_ID', u'5dbff3d57b48b12e7aaf5e94'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.16'), ('sub-component', 'aos-ns'), ('JP_ID', u'5dbff3d97b48b12e7aaf5e98'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.16'), ('sub-component', 'vm-management'), ('JP_ID', u'5dbff3dc7b48b12e7aaf5e9c'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.16'), ('sub-component', 'v3-vm-management'), ('JP_ID', u'5dbff3de7b48b12e7aaf5e9e'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.16'), ('sub-component', 'webhooks'), ('JP_ID', u'5dbff3e07b48b12e7aaf5ea1'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.16'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dbff3e27b48b12e7aaf5ea3'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_ACLI_Scheduling_5.16'), ('sub-component', 'scheduler-acli'), ('JP_ID', u'5dbff3e37b48b12e7aaf5ea5'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Storage_Persona_5.16'), ('sub-component', 'storage-persona'), ('JP_ID', u'5dbff3e57b48b12e7aaf5ea7'), ('max_dep', [u'max_deployments__1'])]),
           #OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_Defrag_5.16'), ('sub-component', 'storage-persona'), ('JP_ID', u'5dbff3e77b48b12e7aaf5ea9'), ('max_dep', [u'max_deployments__1'])])
           ],
 'NO-PC-HA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff3d77b48b12e7aaf5e96'), ('max_dep', [u'max_deployments__1'])])],
 'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.16'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dbff3c67b48b12e7aaf5e84'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.16'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dbff3c87b48b12e7aaf5e86'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.16'), ('sub-component', 'metropolis'), ('JP_ID', u'5dbff3c97b48b12e7aaf5e88'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.16'), ('sub-component', 'metropolis'), ('JP_ID', u'5dbff3cb7b48b12e7aaf5e8a'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.16'), ('sub-component', 'audit'), ('JP_ID', u'5dbff3cd7b48b12e7aaf5e8c'), ('max_dep', [u'max_deployments__1'])])],
 'PC-CATALOG': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.16'), ('sub-component', 'catalog'), ('JP_ID', u'5dbff3917b48b12d57056bc4'), ('max_dep', [u'max_deployments__1'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_5.16'), ('sub-component', 'catalog'), ('JP_ID', u'5dbff3947b48b12d57056bc6'), ('max_dep', [u'max_deployments__3'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_5.16'), ('sub-component', 'catalog'), ('JP_ID', u'5dbff3b07b48b131b2c656c1'), ('max_dep', [u'max_deployments__2'])])],
 'PC-CATALOG-HYPERVISOR-ANY': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.16'), ('sub-component', 'catalog'), ('JP_ID', u'5dbff3c47b48b12e7aaf5e82'), ('max_dep', [u'max_deployments__6'])])],
 'SCHEDULER-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_1_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff44b7b48b134e56ef9d9'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_2_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff44d7b48b134e56ef9db'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_3_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff44f7b48b134e56ef9dd'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_1_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff4517b48b134e56ef9df'), ('max_dep', [u'max_deployments__10'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_2_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff4687b48b1364de8e5f0'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_3_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff4697b48b1364de8e5f2'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_1_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff46b7b48b1364de8e5f4'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_2_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff46d7b48b1364de8e5f7'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_Set_1_5.16'), ('sub-component', 'scheduler'), ('JP_ID', u'5dbff46f7b48b1364de8e5f9'), ('max_dep', [u'max_deployments__2'])])],
 'VNUMA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.16'), ('sub-component', 'vnuma'), ('JP_ID', u'5dbff3fd7b48b12e7aaf5eb1'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.16'), ('sub-component', 'vnuma'), ('JP_ID', u'5dbff3ff7b48b12e7aaf5eb3'), ('max_dep', [u'max_deployments__1'])])],
 'Xi-MGMT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6906_5.16'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dbff4017b48b12e7aaf5eb5'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Xi_Telemetry_FEAT_4361_5.16'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dbff4037b48b12e7aaf5eb7'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6626_5.16'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dbff4047b48b12e7aaf5eb9'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_API_5.16'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dbff4067b48b12e7aaf5ebb'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_OP-xi_API_5.16'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dbff4077b48b12e7aaf5ebd'), ('max_dep', [u'max_deployments__1'])])]
}


# UHURA_JPS_5_16 = {
#     'NO-PC-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__REST_5.16'), ('JP_ID', u'5da7625d7b48b181bc6813b4')]),
#                  OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__RPC_5.16'), ('JP_ID', u'5da7625f7b48b181bc6813bb')]),
#                  OrderedDict([('JP_NAME', u'Regression_Uhura__AHV__UI_5.16'), ('JP_ID', u'5da762627b48b181bc6813bd')])],
#     'NO-PC-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__RPC_5.16'), ('JP_ID', u'5da762517b48b181bc68138e')]),
#                    OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__REST_5.16'), ('JP_ID', u'5da762537b48b181bc681390')]),
#                    OrderedDict([('JP_NAME', u'Regression_Uhura__ESX__UI_5.16'), ('JP_ID', u'5da762567b48b181bc681392')]),
#                    OrderedDict([('JP_NAME', u'Regression_Uhura__ManagementServer_5.16'), ('JP_ID', u'5da762587b48b181bc6813a9')]),
#                    OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-3370_5.16'), ('JP_ID', u'5da7625b7b48b181bc6813b2')])],
#     'NS-NO-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura__Ergon__NS_5.16'), ('JP_ID', u'5da7626b7b48b181bc6813c5')])],
#     'NS-WITH-VC': [OrderedDict([('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.16'), ('JP_ID', u'5da762697b48b181bc6813c3')])],
#     'PC': [OrderedDict([('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.16'), ('JP_ID', u'5da762647b48b181bc6813bf')]),
#         OrderedDict([('JP_NAME', u'Regression_Uhura_GuestCustomization_5.16'), ('JP_ID', u'5da762677b48b181bc6813c1')])]
# }


UHURA_JPS_5_16 = {
    'NO-PC-NO-VC': [
    	OrderedDict([('max_dep', [u'max_deployments__1']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__REST_5.16'), ('JP_ID', u'5da7625d7b48b181bc6813b4')]),
    	OrderedDict([('max_dep', [u'max_deployments__2']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__RPC_5.16'), ('JP_ID', u'5da7625f7b48b181bc6813bb')]),
    	OrderedDict([('max_dep', [u'max_deployments__1']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__UI_5.16'), ('JP_ID', u'5da762627b48b181bc6813bd')])
    ],
    'NO-PC-WITH-VC': [
    			OrderedDict([('max_dep', [u'max_deployments__3']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__RPC_5.16'), ('JP_ID', u'5da762517b48b181bc68138e')]),
                OrderedDict([('max_dep', [u'max_deployments__2']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__REST_5.16'), ('JP_ID', u'5da762537b48b181bc681390')]),
                OrderedDict([('max_dep', [u'max_deployments__1']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__UI_5.16'), ('JP_ID', u'5da762567b48b181bc681392')]),
                OrderedDict([('max_dep', [u'max_deployments__2']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ManagementServer_5.16'), ('JP_ID', u'5da762587b48b181bc6813a9')]),
                OrderedDict([('max_dep', [u'max_deployments__1']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-3370_5.16'), ('JP_ID', u'5da7625b7b48b181bc6813b2')])
    ],
    'NS-NO-VC': [
    			OrderedDict([('max_dep', [u'max_deployments__1']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__Ergon__NS_5.16'), ('JP_ID', u'5da7626b7b48b181bc6813c5')])
    ],
    'NS-WITH-VC': [
    	OrderedDict([('max_dep', [u'max_deployments__1']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.16'), ('JP_ID', u'5da762697b48b181bc6813c3')])
    ],
    'PC': [
    	OrderedDict([('max_dep', [u'max_deployments__1']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.16'), ('JP_ID', u'5da762647b48b181bc6813bf')]),
        OrderedDict([('max_dep', [u'max_deployments__3']), ('sub-component', 'uhura'), ('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GuestCustomization_5.16'), ('JP_ID', u'5da762677b48b181bc6813c1')])
    ]
}

ACROPOLIS_JPS_5_11_2 = {
    'GPU': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.11.2'), ('sub-component', 'gpu'), ('JP_ID', u'5dcf96d12bc0c4598dfc01ad'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.11.2'), ('sub-component', 'gpu'), ('JP_ID', u'5dcf96e98e79ce315b217ab4'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.11.2'), ('sub-component', 'gpu'), ('JP_ID', u'5dcf96d52bc0c4597f743edb'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_1_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96f37b48b13d51e6297a'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_2_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96f47b48b13d44d3b13e'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_3_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96fed24d82a14689054a'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_4_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf9700d24d82a130442b51'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_5_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96ec2bc0c45983f87633'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_6_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96ee2bc0c459933b3e7f'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_1_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf9706d24d82a13936f157'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_2_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf97007b48b13d4394b3eb'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_1_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf9709d24d82a1448cedbc'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_2_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf970cd24d82a13f20a6a0'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_1_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96f72bc0c4599055c447'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_2_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96f92bc0c45983f87638'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_3_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96fb2bc0c4598a2e48b5'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_1_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf96fe2bc0c4597c585650'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_2_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf970e7b48b13d55f009e8'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_3_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf97117b48b13d4dbc4f61'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_4_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf97042bc0c4598eb6ab33'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_5_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf971cd24d82a13af63e1e'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_6_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf971dd24d82a13691e532'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_7_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf97092bc0c45994aa812f'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_1_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf970b2bc0c4598b652c78'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_2_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf970d2bc0c45983f8763a'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_1_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf970e2bc0c459895d6992'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_2_5.11.2'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dcf9726d24d82a146890551'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OTHERS': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.11.2'), ('sub-component', 'ahv-ns'), ('JP_ID', u'5dcf96c77b48b13d426e24ba'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.11.2'), ('sub-component', 'api-stress'), ('JP_ID', u'5dcf96d0d24d82a12d74a748'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.11.2'), ('sub-component', 'frodo'), ('JP_ID', u'5dcf96bc2bc0c4597d8952d9'), ('max_dep', [u'max_deployments__5'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.11.2'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dcf96d4d24d82a13f20a698'), ('max_dep', [u'max_deployments__3'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.11.2'), ('sub-component', 'vnuma'), ('JP_ID', u'5dcf96cf7b48b13d55f009e0'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.11.2'), ('sub-component', 'aos-ns'), ('JP_ID', u'5dcf96c42bc0c4598eb6ab27'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.11.2'), ('sub-component', 'vm-management'), ('JP_ID', u'5dcf96ddd24d82a12c342a5d'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.11.2'), ('sub-component', 'v3-vm-management'), ('JP_ID', u'5dcf96d77b48b13d3dee5a32'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.11.2'), ('sub-component', 'webhooks'), ('JP_ID', u'5dcf96e1d24d82a13691e525'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.11.2'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dcf96cc2bc0c4598c3cb496'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_ACLI_Scheduling_5.11.2'), ('sub-component', 'scheduler-acli'), ('JP_ID', u'5dcf96ce2bc0c45997d344ea'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Storage_Persona_5.11.2'), ('sub-component', 'storage-persona'), ('JP_ID', u'5dcf96e6d24d82a149240354'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC-HA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf96d8d24d82a1314bc910'), ('max_dep', [u'max_deployments__1'])])],
 'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.11.2'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dcf96c48e79ce37f6cdb802'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.11.2'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dcf96c6d24d82a12c342a5a'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.11.2'), ('sub-component', 'metropolis'), ('JP_ID', u'5dcf96b12bc0c4598c3cb48d'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.11.2'), ('sub-component', 'metropolis'), ('JP_ID', u'5dcf96cad24d82a130442b46'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.11.2'), ('sub-component', 'audit'), ('JP_ID', u'5dcf96cc8e79ce331727e6ee'), ('max_dep', [u'max_deployments__1'])])],
 'PC-CATALOG': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.11.2'), ('sub-component', 'catalog'), ('JP_ID', u'5dcf96a72bc0c4edcae23554'), ('max_dep', [u'max_deployments__1'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_5.11.2'), ('sub-component', 'catalog'), ('JP_ID', u'5dcf96bfd24d82a13372af9e'), ('max_dep', [u'max_deployments__3'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_5.11.2'), ('sub-component', 'catalog'), ('JP_ID', u'5dcf96c08e79ce3155609e13'), ('max_dep', [u'max_deployments__2'])])],
 'PC-CATALOG-HYPERVISOR-ANY': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.11.2'), ('sub-component', 'catalog'), ('JP_ID', u'5dcf96ac2bc0c4599055c43d'), ('max_dep', [u'max_deployments__6'])])],
 'SCHEDULER-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_1_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf9728d24d82a13936f15f'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_2_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf972ad24d82a149240368'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_3_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf97162bc0c4598158e6ca'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_1_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf972fd24d82a14105386a'), ('max_dep', [u'max_deployments__10'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_2_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf9730d24d82a145540ca3'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_3_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf9732d24d82a146890555'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_1_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf971e2bc0c4597f743ee5'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_2_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf97368e79ce31660fa056'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_Set_1_5.11.2'), ('sub-component', 'scheduler'), ('JP_ID', u'5dcf97388e79cecb25759685'), ('max_dep', [u'max_deployments__2'])])],
 'VNUMA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.11.2'), ('sub-component', 'vnuma'), ('JP_ID', u'5dcf96d92bc0c459933b3e7a'), ('max_dep', [u'max_deployments__1'])])],
 'Xi-MGMT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6906_5.11.2'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dcf96f18e79ce316c37605d'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Xi_Telemetry_FEAT_4361_5.11.2'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dcf96dc2bc0c45979589b5f'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6626_5.11.2'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dcf96f4d24d82a130442b4e'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_API_5.11.2'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dcf96e02bc0c45991d3a7c6'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_OP-xi_API_5.11.2'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dcf96f17b48b13d41bec744'), ('max_dep', [u'max_deployments__1'])])]
 }

ACROPOLIS_JPS_5_11_3 = {
    'GPU': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.11.3'), ('sub-component', 'gpu'), ('JP_ID', u'5dce199e8e79ce3156eeea65'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.11.3'), ('sub-component', 'gpu'), ('JP_ID', u'5dce199f8e79ce3161d3b7f7'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.11.3'), ('sub-component', 'gpu'), ('JP_ID', u'5dce19a1d24d82219034071e'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_1_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19ad8e79ce3168280b25'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_2_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19aa7b48b13d3c7c9215'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_3_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce198c2bc0c4598dfbc7df'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_4_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19b2d24d822199f38519'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_5_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19af7b48b13d3c7c9217'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_6_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19b17b48b13d3e9557ba'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_1_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19b8d24d82219c99b224'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_2_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19b98e79ce31624770d1'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_1_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19bb8e79ce316368e6be'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_2_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19bd8e79ce315e4d1105'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_1_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19bfd24d8221a77bd1d8'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_2_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19c1d24d8221a77bd1da'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_3_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19be7b48b13d54fb0825'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_1_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19bf7b48b13d36bdf88e'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_2_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19c17b48b13d4ff3cf6d'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_3_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19c8d24d822196d130dd'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_4_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19a52bc0c4597aea0172'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_5_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19a72bc0c45991d36db9'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_6_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19a92bc0c4598dfbc7e2'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_7_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19ced24d8221a5c04874'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_1_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19d0d24d8221a033777d'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_2_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19ce7b48b13d49488ad4'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_1_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19d4d24d8221a77bd1e2'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_2_5.11.3'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5dce19d27b48b13d51e5fb49'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OTHERS': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.11.3'), ('sub-component', 'ahv-ns'), ('JP_ID', u'5dce19622bc0c4597ea60f48'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.11.3'), ('sub-component', 'api-stress'), ('JP_ID', u'5dce1988d24d82219233e016'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.11.3'), ('sub-component', 'frodo'), ('JP_ID', u'5dce19898e79ce3161d3b7f0'), ('max_dep', [u'max_deployments__5'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.11.3'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dce198b8e79ce3161d3b7f2'), ('max_dep', [u'max_deployments__3'])]),
                     #OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Host_Agent_Test_5.11.3'), ('sub-component', 'host-agent'), ('JP_ID', u'5dce19887b48b13d41be9928'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.11.3'), ('sub-component', 'vnuma'), ('JP_ID', u'5dce198e8e79ce316c3726dd'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.11.3'), ('sub-component', 'aos-ns'), ('JP_ID', u'5dce19928e79ce31742ca3d4'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.11.3'), ('sub-component', 'vm-management'), ('JP_ID', u'5dce19938e79ce316c3726df'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.11.3'), ('sub-component', 'v3-vm-management'), ('JP_ID', u'5dce1995d24d82219034071b'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.11.3'), ('sub-component', 'webhooks'), ('JP_ID', u'5dce19722bc0c4597c581c4e'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.11.3'), ('sub-component', 'ahv-co'), ('JP_ID', u'5dce19988e79ce31660f673c'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_ACLI_Scheduling_5.11.3'), ('sub-component', 'scheduler-acli'), ('JP_ID', u'5dce19957b48b13d3e9557b6'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Storage_Persona_5.11.3'), ('sub-component', 'storage-persona'), ('JP_ID', u'5dce19772bc0c4598a2e0d64'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC-HA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce1990d24d8221ae74956f'), ('max_dep', [u'max_deployments__1'])])],
 'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.11.3'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dce197e8e79ce316d6135f3'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.11.3'), ('sub-component', 'batch-vms'), ('JP_ID', u'5dce197b7b48b13d3dee2b1b'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.11.3'), ('sub-component', 'metropolis'), ('JP_ID', u'5dce19828e79ce315b213edf'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.11.3'), ('sub-component', 'metropolis'), ('JP_ID', u'5dce19838e79ce31556063fb'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.11.3'), ('sub-component', 'audit'), ('JP_ID', u'5dce19848e79ce3168280b1a'), ('max_dep', [u'max_deployments__1'])])],
 'PC-CATALOG': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.11.3'), ('sub-component', 'catalog'), ('JP_ID', u'5dce1978d24d82219233e012'), ('max_dep', [u'max_deployments__1'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_5.11.3'), ('sub-component', 'catalog'), ('JP_ID', u'5dce19798e79ce3165b4ee4f'), ('max_dep', [u'max_deployments__3'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_5.11.3'), ('sub-component', 'catalog'), ('JP_ID', u'5dce197b8e79ce31660f6739'), ('max_dep', [u'max_deployments__2'])])],
 'PC-CATALOG-HYPERVISOR-ANY': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.11.3'), ('sub-component', 'catalog'), ('JP_ID', u'5dce197d8e79ce31642f65ec'), ('max_dep', [u'max_deployments__6'])])],
 'SCHEDULER-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_1_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19d88e79ce31624770d7'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_2_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19b62bc0c459827d361c'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_3_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19dcd24d8221ae749576'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_1_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19b92bc0c45984520fa2'), ('max_dep', [u'max_deployments__10'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_2_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19db7b48b13d4394870c'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_3_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19dd7b48b13d44d3839c'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_1_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19df7b48b13d44d3839f'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_2_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19c12bc0c459933b043c'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_Set_1_5.11.3'), ('sub-component', 'scheduler'), ('JP_ID', u'5dce19e78e79ce315ab87fdd'), ('max_dep', [u'max_deployments__2'])])],
 'VNUMA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.11.3'), ('sub-component', 'vnuma'), ('JP_ID', u'5dce199e7b48b13d3aa171c0'), ('max_dep', [u'max_deployments__1'])])],
 'Xi-MGMT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6906_5.11.3'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dce19a5d24d8221978df931'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Xi_Telemetry_FEAT_4361_5.11.3'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dce19a68e79ce315f31af7e'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6626_5.11.3'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dce19a8d24d8221a6d6f618'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_API_5.11.3'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dce19a57b48b13d3dee2b22'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_OP-xi_API_5.11.3'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5dce19ac8e79ce3167567cec'), ('max_dep', [u'max_deployments__1'])])]
 }

UHURA_JPS_5_11_3 = {
    'NO-PC-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__REST_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77bd8e79ce31742c8972'), ('max_dep', [u'max_deployments__1'])]),
                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__RPC_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77bc7b48b13d50df6d3b'), ('max_dep', [u'max_deployments__2'])]),
                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__UI_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77c28e79ce316d611b32'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__RPC_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd779e2bc0c45997d2f086'), ('max_dep', [u'max_deployments__3'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__REST_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77a02bc0c4597824b824'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__UI_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77b8d24d8221a213b400'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ManagementServer_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77b67b48b13d494875ad'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-3370_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77b87b48b13d39a63bc9'), ('max_dep', [u'max_deployments__1'])])],
 'NS-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__Ergon__NS_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77b42bc0c4598dfbad8e'), ('max_dep', [u'max_deployments__1'])])],
 'NS-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77c8d24d8221a430f4b7'), ('max_dep', [u'max_deployments__1'])])],
 'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77af2bc0c459960311ab'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GuestCustomization_5.11.3'), ('sub-component', 'uhura'), ('JP_ID', u'5dcd77b12bc0c45994aa2ec6'), ('max_dep', [u'max_deployments__3'])])]
 }

ACROPOLIS_JPS_5_17 = {
'GPU': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Gpu_Passthrough_5.17'), ('sub-component', 'gpu'), ('JP_ID', u'5df29af72bc0c452bb83cf18'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_VGpu_5.17'), ('sub-component', 'gpu'), ('JP_ID', u'5df29af98e79ce409636abde'), ('max_dep', [u'max_deployments__1'])]),
         OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_GPU_Compute_Mode_5.17'), ('sub-component', 'gpu'), ('JP_ID', u'5df29afb8e79ce409f4bbc22'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_1_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b08d24d824d39bd102d'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_2_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b0ad24d824d41b8d261'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_3_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b0b2bc0c452a853edf3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_4_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b0d2bc0c452b812fa74'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_5_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b0f2bc0c4bc5e577f08'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LLC_6_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b10d24d824d38c6a74d'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_1_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b128e79ce409e38dfec'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WLC_2_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b148e79ce40a4377474'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_1_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b162bc0c42197bd69a3'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WI_2_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b18d24d824d3f651f93'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_1_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b1ad24d824d2e321d6f'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_2_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b1b2bc0c452a5e98c89'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LI_3_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b1d8e79ceaf02fadce8'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_1_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b1f8e79cef12c36db7f'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_2_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b218e79ce4030e0f2be'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_3_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b232bc0c452b61bfc55'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_4_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b248e79ce408d1f4c81'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_5_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b262bc0c4bc5e577f11'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_6_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b282bc0c452bf56d6e4'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_LVDT_7_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b2a2bc0c452b56c7642'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_1_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b2cd24d824d2f25f741'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVDT_2_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b2ed24d824d2f25f744'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_1_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b2fd24d824d4b0719ad'), ('max_dep', [u'max_deployments__1'])]),
                  OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Guest_OS_WVT_2_5.17'), ('sub-component', 'ahv-guest-os'), ('JP_ID', u'5df29b312bc0c452a3780557'), ('max_dep', [u'max_deployments__1'])])],
 'GUEST-OS-OTHERS': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AHV_NS_5.17'), ('sub-component', 'ahv-ns'), ('JP_ID', u'5df29ae08e79ce4092719fb2'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_stress_general_5.17'), ('sub-component', 'api-stress'), ('JP_ID', u'5df29ae28e79ceec781e8bb7'), ('max_dep', [u'max_deployments__1'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Frodo_5.17'), ('sub-component', 'frodo'), ('JP_ID', u'5df29ae42bc0c422d54938ba'), ('max_dep', [u'max_deployments__5'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AHV_5.17'), ('sub-component', 'ahv-co'), ('JP_ID', u'5df29ae6d24d824d44021418'), ('max_dep', [u'max_deployments__3'])]),
                     OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_api_Vcpu_stress_5.17'), ('sub-component', 'vnuma'), ('JP_ID', u'5df29ae8d24d824d43b21ac6'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_AOS_NS_5.17'), ('sub-component', 'aos-ns'), ('JP_ID', u'5df29aeb2bc0c452b0ca3cc7'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Acropolis_Vm_Management_5.17'), ('sub-component', 'vm-management'), ('JP_ID', u'5df29aed2bc0c424005db521'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_V3_Vm_Management_5.17'), ('sub-component', 'v3-vm-management'), ('JP_ID', u'5df29aef2bc0c452aae1f1ce'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Webhooks_5.17'), ('sub-component', 'webhooks'), ('JP_ID', u'5df29af12bc0c452b0ca3cc9'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_CO_AOS_5.17'), ('sub-component', 'ahv-co'), ('JP_ID', u'5df29af22bc0c452b97d3b16'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_ACLI_Scheduling_5.17'), ('sub-component', 'scheduler-acli'), ('JP_ID', u'5df29af48e79ceec781e8bbf'), ('max_dep', [u'max_deployments__1'])]),
           OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Storage_Persona_5.17'), ('sub-component', 'storage-persona'), ('JP_ID', u'5df29af62bc0c452af37b1b3'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC-HA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Twonode_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29ae98e79ce748d3e10cb'), ('max_dep', [u'max_deployments__1'])])],
 'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_5.17'), ('sub-component', 'batch-vms'), ('JP_ID', u'5df29ad72bc0c452bb83cf0c'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_batch_vm_pc_Xi_5.17'), ('sub-component', 'batch-vms'), ('JP_ID', u'5df29ad92bc0c452bb83cf0f'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_xi_5.17'), ('sub-component', 'metropolis'), ('JP_ID', u'5df29adbd24d824d39bd1022'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Metropolis_5.17'), ('sub-component', 'metropolis'), ('JP_ID', u'5df29add2bc0c452b812fa66'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Audit_5.17'), ('sub-component', 'audit'), ('JP_ID', u'5df29ade8e79ce6983be27dd'), ('max_dep', [u'max_deployments__1'])])],
 'PC-CATALOG': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_remote_seed_5.17'), ('sub-component', 'catalog'), ('JP_ID', u'5df29ad08e79ce40a859e211'), ('max_dep', [u'max_deployments__1'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Cluster_Selection_5.17'), ('sub-component', 'catalog'), ('JP_ID', u'5df29ad28e79ce87cb2564d7'), ('max_dep', [u'max_deployments__3'])]),
                OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_Optimized_Checkout_5.17'), ('sub-component', 'catalog'), ('JP_ID', u'5df29ad32bc0c452a72d5c3b'), ('max_dep', [u'max_deployments__2'])])],
 'PC-CATALOG-HYPERVISOR-ANY': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Catalog_5.17'), ('sub-component', 'catalog'), ('JP_ID', u'5df29ad5d24d824d46f51697'), ('max_dep', [u'max_deployments__6'])])],
 'SCHEDULER-OPT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_1_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b328e79ce409981f385'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_2_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b358e79ce40a2b7b0d1'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Affinity_scheduling_policies_Set_3_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b37d24d824d3b0ccc6e'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_1_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b39d24d824d315aabe8'), ('max_dep', [u'max_deployments__10'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_2_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b3b8e79ce5f3b75b0dc'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_HA_Set_3_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b3c2bc0c452b0ca3cd7'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_1_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b3f8e79ce40a859e238'), ('max_dep', [u'max_deployments__5'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Ads_Set_2_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b40d24d824d357f59a8'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Scheduler_During_Upgrades_Set_1_5.17'), ('sub-component', 'scheduler'), ('JP_ID', u'5df29b428e79ce408f91fcdb'), ('max_dep', [u'max_deployments__2'])])],
 'VNUMA': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Vnuma_5.17'), ('sub-component', 'vnuma'), ('JP_ID', u'5df29afd2bc0c452a3780549'), ('max_dep', [u'max_deployments__1'])])],
 'Xi-MGMT': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6906_5.17'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5df29aff8e79ce409f4bbc24'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_Xi_Telemetry_FEAT_4361_5.17'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5df29b002bc0c452b97d3b19'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_API_Tests_FEAT-6626_5.17'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5df29b02d24d824d4aae834a'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_API_5.17'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5df29b04d24d824d40ac6f3b'), ('max_dep', [u'max_deployments__1'])]),
             OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Acropolis_MTS_Nutest_XI_Pairing_OP-xi_API_5.17'), ('sub-component', 'xi-manageability'), ('JP_ID', u'5df29b06d24d824d450188a5'), ('max_dep', [u'max_deployments__1'])])]
 }


UHURA_JPS_5_17 = {
    'NO-PC-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__REST_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c7f8e79ce40a1c462a3'), ('max_dep', [u'max_deployments__1'])]),
                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__RPC_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c812bc0c452ae228783'), ('max_dep', [u'max_deployments__2'])]),
                 OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__AHV__UI_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c822bc0c452b97cb6ea'), ('max_dep', [u'max_deployments__1'])])],
 'NO-PC-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__RPC_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c788e79ce5f3b75280d'), ('max_dep', [u'max_deployments__3'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__REST_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c798e79ce408ee7f10e'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ESX__UI_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c7b8e79ce40a7991b59'), ('max_dep', [u'max_deployments__1'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__ManagementServer_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c7c2bc0c452bb834b09'), ('max_dep', [u'max_deployments__2'])]),
                   OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-3370_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c7e2bc0c452a48d7a01'), ('max_dep', [u'max_deployments__1'])])],
 'NS-NO-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura__Ergon__NS_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c8a8e79ce40a8595655'), ('max_dep', [u'max_deployments__1'])])],
 'NS-WITH-VC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GoldSuite_NS_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c878e79ce40a436ead4'), ('max_dep', [u'max_deployments__1'])])],
 'PC': [OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_FEAT-6978_v3_clone_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c848e79ce409271159c'), ('max_dep', [u'max_deployments__1'])]),
        OrderedDict([('category', 'reg-handedover'), ('JP_NAME', u'Regression_Uhura_GuestCustomization_5.17'), ('sub-component', 'uhura'), ('JP_ID', u'5df07c868e79ce409f4b32ae'), ('max_dep', [u'max_deployments__3'])])]
}

# ACROPOLIS_JPS_MAJOR = ACROPOLIS_JPS_5_10_2.copy()
# UHURA_JPS_MAJOR = UHURA_JPS_5_10_2.copy()

#ACROPOLIS_JPS_LTS = ACROPOLIS_JPS_LTS_5_5_8.copy()
#UHURA_JPS_LTS = UHURA_JPS_LTS_5_5_8.copy()

# UHURA_JPS_LTS = UHURA_JPS_LTS_5_5_9.copy()
# ACROPOLIS_JPS_LTS = ACROPOLIS_JPS_5_5_9.copy()


# ACROPOLIS_JPS_MAJOR = ACROPOLIS_JPS_5_11.copy()
# UHURA_JPS_MAJOR = UHURA_JPS_5_11.copy()

# ACROPOLIS_JPS_MAJOR = ACROPOLIS_JPS_5_16.copy()
# UHURA_JPS_MAJOR = UHURA_JPS_5_16.copy()


# UHURA_JPS_MAJOR = UHURA_JPS_5_17.copy()
# ACROPOLIS_JPS_MAJOR = ACROPOLIS_JPS_5_17.copy()

# ACROPOLIS_JPS_MINOR = ACROPOLIS_JPS_5_11_1.copy()
# UHURA_JPS_MINOR = UHURA_JPS_5_11_1.copy()


#ACROPOLIS_JPS_MINOR = ACROPOLIS_JPS_5_10_9.copy()
# UHURA_JPS_MINOR = UHURA_JPS_5_10_9.copy()

#ACROPOLIS_JPS_MINOR = ACROPOLIS_JPS_5_11_2.copy()


#ACROPOLIS_JPS_MINOR = ACROPOLIS_JPS_5_11_3.copy()
# UHURA_JPS_MINOR = UHURA_JPS_5_11_3.copy()
