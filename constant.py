ENDOR_PC_BUILD_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/'
MASTER_KWARGS = {
    "branch": "MASTER",
    "nos_branch": "master",
    "pc_branch": "master",
    "nos_commit": "b322f2711c7293ae1adc2e9133c99a8cca4838cf",
    "pc_commit": "b322f2711c7293ae1adc2e9133c99a8cca4838cf",
    "build_type": 'opt',
    "nutest_branch": "master",
    "obelix_branch": None
}
KWARGS_5_18 = {
    "branch": "5.18",
    "nos_branch": "euphrates-5.18-stable",
    "nos_commit": "0770d2d06eb07bb8498e685305ce63c4f27dbf3b",
    "build_type": 'release',
    "nutest_branch": "euphrates-5.18-stable",
    "obelix_branch": "dogmatix"
}
KWARGS_5_19 = {
    "branch": "5.19",
    "pc_branch": "euphrates-5.19-stable-pc-0",
    "pc_commit": "9db9b2f68c5b16c77d26f51c7786829935a28e1e",
    "nos_branch": "euphrates-5.19-stable",
    "nos_commit": "9ed71ed472826fb92fbf4e16b7e82e8d47746e58",
    "build_type": 'release',
    "nutest_branch": "euphrates-5.19-stable",
    "obelix_branch": "dogmatix_5.19"
}
KWARGS_5_15_1 = {
    "branch": "5.15.1",
    "nos_branch": "euphrates-5.15.1-stable",
    "nos_commit": "8d3f441f3128f6df0d636cd37f70d6562be91280",
    "build_type": 'release',
    "nutest_branch": "euphrates-5.15-stable",
    "obelix_branch": "obelix"
}
GOS_PATCH_MASTER = u'https://gerrit.eng.nutanix.com/changes/379816/revisions/27ebe5c9daeebd81563273efb4c7b1788dfc1df8/patch?zip'
# GOS_PATCH_MASTER = u'https://gerrit.eng.nutanix.com/changes/406605/revisions/9bf1fcfca6f44cfb3b6df7c428bb6d3206617ca9/patch?zip'
BUILD_NOS_URL = 'http://endor.dyn.nutanix.com/builds/nos-builds/{0}/{1}/x86_64/release/tar/cvm/'
BUILD_PC_URL = 'http://endor.dyn.nutanix.com/builds/PC-builds/{0}/{1}/{2}/'
# BUILD_HYPERVISOR_URL = 'http://endor.dyn.nutanix.com/builds/nos-builds/euphrates-5.19-stable/9ed71ed472826fb92fbf4e16b7e82e8d47746e58/x86_64/release/tar/AHV/20190916.101596/iso/installed-el7.nutanix.20190916.101596.qcow2'
BUILD_HYPERVISOR_URL = 'http://endor.dyn.nutanix.com/builds/nos-builds/master/fa84da8e7d44a313afcf7e9664c3c87eb96c6419/x86_64/release/tar/AHV/20201007.101614/iso/installed-el7.nutanix.20201007.101614.qcow2'
