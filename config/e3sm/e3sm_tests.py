# Here are the tests belonging to e3sm suites. Format is
# <test>.<grid>.<compset>.
# suite_name -> (inherits_from, timelimit, [test [, mods[, machines]]])
#   To elaborate, if no mods are needed, a string representing the testname is all that is needed.
#   If testmods are needed, a 2-ple must be provided  (test, mods)
#   If you want to restrict the test mods to certain machines, than a 3-ple is needed (test, mods, [machines])
_TEST_SUITES = {
    "cime_tiny" : (None, "0:10:00",
                   ("ERS.f19_g16_rx1.A",
                    "NCK.f19_g16_rx1.A")
                   ),

    "cime_test_only_pass" : (None, "0:10:00",
                   ("TESTRUNPASS_P1.f19_g16_rx1.A",
                    "TESTRUNPASS_P1.ne30_g16_rx1.A",
                    "TESTRUNPASS_P1.f45_g37_rx1.A")
                   ),

    "cime_test_only_slow_pass" : (None, "0:10:00",
                   ("TESTRUNSLOWPASS_P1.f19_g16_rx1.A",
                    "TESTRUNSLOWPASS_P1.ne30_g16_rx1.A",
                    "TESTRUNSLOWPASS_P1.f45_g37_rx1.A")
                   ),

    "cime_test_only" : (None, "0:10:00",
                   ("TESTBUILDFAIL_P1.f19_g16_rx1.A",
                    "TESTBUILDFAILEXC_P1.f19_g16_rx1.A",
                    "TESTRUNFAIL_P1.f19_g16_rx1.A",
                    "TESTRUNFAILEXC_P1.f19_g16_rx1.A",
                    "TESTRUNPASS_P1.f19_g16_rx1.A",
                    "TESTTESTDIFF_P1.f19_g16_rx1.A",
                    "TESTMEMLEAKFAIL_P1.f09_g16.X",
                    "TESTMEMLEAKPASS_P1.f09_g16.X")
                   ),

    "cime_developer" : (None, "0:15:00",
                            ("NCK_Ld3.f45_g37_rx1.A",
                             "ERI.f09_g16.X",
                             "ERIO.f09_g16.X",
                             "SEQ_Ln9.f19_g16_rx1.A",
                             ("ERS.ne30_g16_rx1.A","drv-y100k"),
                             "IRT_N2.f19_g16_rx1.A",
                             "ERR.f45_g37_rx1.A",
                             "ERP.f45_g37_rx1.A",
                             "SMS_D_Ln9.f19_g16_rx1.A",
                             "DAE.f19_f19.A",
                             "PET_P4.f19_f19.A",
                             "SMS.T42_T42.S",
                             "PRE.f19_f19.ADESP",
                             "PRE.f19_f19.ADESP_TEST",
                             "MCC_P1.f19_g16_rx1.A",
                             "LDSTA.f45_g37_rx1.A")
                            ),

    #
    # ACME tests below
    #

    "e3sm_runoff_developer" : (None, "0:45:00",
                             ("ERS.f19_f19.IM1850CLM45CN",
                              "ERS.f19_f19.IMCLM45")
                             ),

    "e3sm_land_developer" : ("e3sm_runoff_developer", "0:45:00",
                             ("ERS.f19_f19.I1850CLM45CN",
                              "ERS.f09_g16.I1850CLM45CN",
                              "ERS.f19_f19.I20TRCLM45CN",
                              "SMS_Ld1.hcru_hcru.I1850CRUCLM45CN",
                             ("ERS.f19_g16.I1850CNECACNTBC" ,"clm-eca"),
                             ("ERS.f19_g16.I1850CNECACTCBC" ,"clm-eca"),
                             ("SMS_Ly2_P1x1.1x1_smallvilleIA.ICLM45CNCROP", "force_netcdf_pio"),
                             ("ERS_Ld3.f45_f45.ICLM45ED","clm-fates"),
                             ("ERS.f19_g16.I1850CLM45","clm-betr"),
                             ("ERS.f19_g16.I1850CLM45","clm-vst"),
                             ("ERS.f09_g16.I1850CLM45CN","clm-bgcinterface"),
                              "ERS.ne11_oQU240.I20TRCLM45",
                             ("ERS.f19_g16.I1850CNRDCTCBC","clm-rd"),
                              "ERS.f09_g16.IMCLM45BC")
                             ),

    "e3sm_atm_developer" : (None, None,
                            ("SMS_D_Ln5.ne4_ne4.FC5",
                             "ERP_Ln9.ne4_ne4.FC5AV1C-L",
                             ("SMS_Ln9.ne4_ne4.FC5AV1C-L", "cam-outfrq9s"),
                             ("SMS.ne4_ne4.FC5AV1C-L", "cam-cosplite"),
                             "SMS_R_Ld5.T42_T42.FSCM5A97",
                             "SMS_D_Ln5.ne4_ne4.FC5AV1C-L")
                            ),

    "e3sm_atm_integration" : (None, None,
                              ("ERS_Ln9.ne4_ne4.FC5" ,
                               "ERP_Ln9.ne4_ne4.FC5AV1C-L-AQUAP",
                               ("PET_Ln5.ne4_ne4.FC5AV1C-L","mach-pet"),
                               "PEM_Ln5.ne4_ne4.FC5AV1C-L",
                               ("SMS_D_Ln5.ne4_ne4.FC5AV1C-L", "cam-cosplite_nhtfrq5"),
                               "REP_Ln5.ne4_ne4.FC5AV1C-L")
                              ),
    #atmopheric tests for extra coverage
    "e3sm_atm_extra_coverage" : (None, None,
                         ("SMS_Lm1.ne4_ne4.FC5AV1C-L",
                          "ERS_Ld31.ne4_ne4.FC5AV1C-L",
                          "ERP_Lm3.ne4_ne4.FC5AV1C-L",
                          "SMS_D_Ln5.ne30_ne30.FC5AV1C-L",
                          ("ERP_Ln5.ne30_ne30.FC5AV1C-L"),
                          "SMS_Ly1.ne4_ne4.FC5AV1C-L")
                         ),
    #atmopheric tests for hi-res
    "e3sm_atm_hi_res" : (None, "01:30:00",
                         (
                          "SMS.ne120_ne120.FC5AV1C-H01A",
                         )),
    #atmopheric tests to mimic low res production runs
    "e3sm_atm_prod" : (None, None,
                       (("SMS_Ln5.ne30_ne30.FC5AV1C-L", "cam-cosplite"),
                        )
                       ),

    "e3sm_developer" : (("e3sm_land_developer","e3sm_atm_developer"), "0:45:00",
                        ("ERS.f19_g16_rx1.A",
                         "ERS.f45_g37_rx1.DTEST",
                         "ERS.ne30_g16_rx1.A",
                         "ERS_IOP.f19_g16_rx1.A",
                         "ERS_IOP.f45_g37_rx1.DTEST",
                         "ERS_IOP.ne30_g16_rx1.A",
                         "ERS_IOP4c.f19_g16_rx1.A",
                         "ERS_IOP4c.ne30_g16_rx1.A",
                         "ERS_IOP4p.f19_g16_rx1.A",
                         "ERS_IOP4p.ne30_g16_rx1.A",
                         "HOMME_P24.f19_g16_rx1.A",
                         "NCK.f19_g16_rx1.A",
                         "SMS.ne30_f19_g16_rx1.A",
                         "ERS_Ld5.T62_oQU120.CMPASO-NYF",
                         "ERS.f09_g16_g.MPASLISIA",
                         "SMS.T62_oQU120_ais20.MPAS_LISIO_TEST",
                         "SMS.f09_g16_a.IGCLM45_MLI"
                        ,("SMS_P12x2.ne4_oQU240.A_WCYCL1850","mach_mods")
                        )),

    "e3sm_integration" : (("e3sm_developer", "e3sm_atm_integration"),"03:00:00",
                          ("ERS.ne11_oQU240.A_WCYCL1850",
		           ("SMS_D_Ld1.ne30_oECv3_ICG.A_WCYCL1850S_CMIP6","v1cmip6"),
                           "ERS_Ln9.ne4_ne4.FC5AV1C-L",
                          #"ERT_Ld31.ne16_g37.B1850C5",#add this line back in with the new correct compset
                           ("PET.f19_g16.X","mach-pet"),
                           ("PET.f45_g37_rx1.A","mach-pet"),
                           ("PET_Ln9_PS.ne30_oECv3_ICG.A_WCYCL1850S","mach-pet"),
                           "PEM_Ln9.ne30_oECv3_ICG.A_WCYCL1850S",
                           "ERP_Ld3.ne30_oECv3_ICG.A_WCYCL1850S",
                           "SEQ_IOP.f19_g16.X",
                           "SMS.f09_g16_a.MPASLIALB",
                           "SMS_D_Ln5.conusx4v1_conusx4v1.FC5AV1C-L",
			   ("SMS.ne30_oECv3.BGCEXP_BCRC_CNPRDCTC_1850","clm-bgcexp"),
                           ("SMS.ne30_oECv3.BGCEXP_BCRC_CNPECACNT_1850","clm-bgcexp"))
                          ),
    #e3sm tests for extra coverage
    "e3sm_extra_coverage" : (("e3sm_atm_extra_coverage",), None,
                             ("SMS_D_Ln5.enax4v1_enax4v1.FC5AV1C-L",
                              "SMS_D_Ln5.twpx4v1_twpx4v1.FC5AV1C-L")),

    #e3sm tests for hi-res
    "e3sm_hi_res" : (("e3sm_atm_hi_res",),None,
                     (
                      ("SMS.ne120_oRRS18v3_ICG.A_WCYCL2000_H01AS", "cam-cosplite"),
                       "SMS.T62_oRRS30to10v3wLI.GMPAS-IAF",
                     )),

    #e3sm tests for RRM grids
    "e3sm_rrm" : (None, None,
                  ("SMS_D_Ln5.conusx4v1_conusx4v1.FC5AV1C-L",
                   "SMS_D_Ln5.enax4v1_enax4v1.FC5AV1C-L",
                   "SMS_D_Ln5.twpx4v1_twpx4v1.FC5AV1C-L")
                 ),

    #e3sm tests to mimic production runs
    "e3sm_prod" : (("e3sm_atm_prod",),None,
                     (
		      ("SMS_Ld2.ne30_oECv3_ICG.A_WCYCL1850S_CMIP6","v1cmip6"),
		      )),

    "fates" : (None, None,
                         ("ERS_Ld9.1x1_brazil.ICLM45ED",
                          "ERS_D_Ld9.1x1_brazil.ICLM45ED",
                          "SMS_D_Lm6.1x1_brazil.ICLM45ED")
                         ),
}
