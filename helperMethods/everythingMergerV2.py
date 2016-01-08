
import os
import os
import csv
import itertools
#change the state number and the name and the savetodirectory list 
stateNumber = 50
stateName = 'maryland2.csv'

#Make sure no to change SAVE_TO_DIRECTORY when pasting in folders
SAVE_TO_DIRECTORY = [\

"/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/21/0",\
"/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/21/200",\
"/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/21/400",\
"/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/21/600",\
"/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/21/800",\

]

for directory in range (0, 8):
    
    for x in range (0, 600):
        try:
            docName = str(x)
            os.chdir(SAVE_TO_DIRECTORY[directory])
            files = filter(os.path.isfile, os.listdir(SAVE_TO_DIRECTORY[directory]))
            files = [os.path.join(SAVE_TO_DIRECTORY[directory], f) for f in files] # add path to each file
            files.sort(key=lambda x: os.path.getmtime(x))
            newest_file = files[x]
            os.rename(newest_file, docName+".csv")
        except:
            print "Finished Renaming"
            pass
    print "Done Renaming"


    completeFile = "/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/21/" + stateName
    listLoad = ["0.csv", "1.csv", "2.csv", "3.csv", "4.csv", "5.csv", "6.csv", "7.csv", "8.csv", "9.csv", "10.csv", "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv", "21.csv", "22.csv", "23.csv", "24.csv", "25.csv", "26.csv", "27.csv", "28.csv", "29.csv", "30.csv", "31.csv", "32.csv", "33.csv", "34.csv", "35.csv", "36.csv", "37.csv", "38.csv", "39.csv", "40.csv", "41.csv", "42.csv", "43.csv", "44.csv", "45.csv", "46.csv", "47.csv", "48.csv", "49.csv", "50.csv", "51.csv", "52.csv", "53.csv", "54.csv", "55.csv", "56.csv", "57.csv", "58.csv", "59.csv", "60.csv", "61.csv", "62.csv", "63.csv", "64.csv", "65.csv", "66.csv", "67.csv", "68.csv", "69.csv", "70.csv", "71.csv", "72.csv", "73.csv", "74.csv", "75.csv", "76.csv", "77.csv", "78.csv", "79.csv", "80.csv", "81.csv", "82.csv", "83.csv", "84.csv", "85.csv", "86.csv", "87.csv", "88.csv", "89.csv", "90.csv", "91.csv", "92.csv", "93.csv", "94.csv", "95.csv", "96.csv", "97.csv", "98.csv", "99.csv", "100.csv", "101.csv", "102.csv", "103.csv", "104.csv", "105.csv", "106.csv", "107.csv", "108.csv", "109.csv", "110.csv", "111.csv", "112.csv", "113.csv", "114.csv", "115.csv", "116.csv", "117.csv", "118.csv", "119.csv", "120.csv", "121.csv", "122.csv", "123.csv", "124.csv", "125.csv", "126.csv", "127.csv", "128.csv", "129.csv", "130.csv", "131.csv", "132.csv", "133.csv", "134.csv", "135.csv", "136.csv", "137.csv", "138.csv", "139.csv", "140.csv", "141.csv", "142.csv", "143.csv", "144.csv", "145.csv", "146.csv", "147.csv", "148.csv", "149.csv", "150.csv", "151.csv", "152.csv", "153.csv", "154.csv", "155.csv", "156.csv", "157.csv", "158.csv", "159.csv", "160.csv", "161.csv", "162.csv", "163.csv", "164.csv", "165.csv", "166.csv", "167.csv", "168.csv", "169.csv", "170.csv", "171.csv", "172.csv", "173.csv", "174.csv", "175.csv", "176.csv", "177.csv", "178.csv", "179.csv", "180.csv", "181.csv", "182.csv", "183.csv", "184.csv", "185.csv", "186.csv", "187.csv", "188.csv", "189.csv", "190.csv", "191.csv", "192.csv", "193.csv", "194.csv", "195.csv", "196.csv", "197.csv", "198.csv", "199.csv", "200.csv", "201.csv", "202.csv", "203.csv", "204.csv", "205.csv", "206.csv", "207.csv", "208.csv", "209.csv", "210.csv", "211.csv", "212.csv", "213.csv", "214.csv", "215.csv", "216.csv", "217.csv", "218.csv", "219.csv", "220.csv", "221.csv", "222.csv", "223.csv", "224.csv", "225.csv", "226.csv", "227.csv", "228.csv", "229.csv", "230.csv", "231.csv", "232.csv", "233.csv", "234.csv", "235.csv", "236.csv", "237.csv", "238.csv", "239.csv", "240.csv", "241.csv", "242.csv", "243.csv", "244.csv", "245.csv", "246.csv", "247.csv", "248.csv", "249.csv", "250.csv", "251.csv", "252.csv", "253.csv", "254.csv", "255.csv", "256.csv", "257.csv", "258.csv", "259.csv", "260.csv", "261.csv", "262.csv", "263.csv", "264.csv", "265.csv", "266.csv", "267.csv", "268.csv", "269.csv", "270.csv", "271.csv", "272.csv", "273.csv", "274.csv", "275.csv", "276.csv", "277.csv", "278.csv", "279.csv", "280.csv", "281.csv", "282.csv", "283.csv", "284.csv", "285.csv", "286.csv", "287.csv", "288.csv", "289.csv", "290.csv", "291.csv", "292.csv", "293.csv", "294.csv", "295.csv", "296.csv", "297.csv", "298.csv", "299.csv", "300.csv", "301.csv", "302.csv", "303.csv", "304.csv", "305.csv", "306.csv", "307.csv", "308.csv", "309.csv", "310.csv", "311.csv", "312.csv", "313.csv", "314.csv", "315.csv", "316.csv", "317.csv", "318.csv", "319.csv", "320.csv", "321.csv", "322.csv", "323.csv", "324.csv", "325.csv", "326.csv", "327.csv", "328.csv", "329.csv", "330.csv", "331.csv", "332.csv", "333.csv", "334.csv", "335.csv", "336.csv", "337.csv", "338.csv", "339.csv", "340.csv", "341.csv", "342.csv", "343.csv", "344.csv", "345.csv", "346.csv", "347.csv", "348.csv", "349.csv", "350.csv", "351.csv", "352.csv", "353.csv", "354.csv", "355.csv", "356.csv", "357.csv", "358.csv", "359.csv", "360.csv", "361.csv", "362.csv", "363.csv", "364.csv", "365.csv", "366.csv", "367.csv", "368.csv", "369.csv", "370.csv", "371.csv", "372.csv", "373.csv", "374.csv", "375.csv", "376.csv", "377.csv", "378.csv", "379.csv", "380.csv", "381.csv", "382.csv", "383.csv", "384.csv", "385.csv", "386.csv", "387.csv", "388.csv", "389.csv", "390.csv", "391.csv", "392.csv", "393.csv", "394.csv", "395.csv", "396.csv", "397.csv", "398.csv", "399.csv", "400.csv", "401.csv", "402.csv", "403.csv", "404.csv", "405.csv", "406.csv", "407.csv", "408.csv", "409.csv", "410.csv", "411.csv", "412.csv", "413.csv", "414.csv", "415.csv", "416.csv", "417.csv", "418.csv", "419.csv", "420.csv", "421.csv", "422.csv", "423.csv", "424.csv", "425.csv", "426.csv", "427.csv", "428.csv", "429.csv", "430.csv", "431.csv", "432.csv", "433.csv", "434.csv", "435.csv", "436.csv", "437.csv", "438.csv", "439.csv", "440.csv", "441.csv", "442.csv", "443.csv", "444.csv", "445.csv", "446.csv", "447.csv", "448.csv", "449.csv", "450.csv", "451.csv", "452.csv", "453.csv", "454.csv", "455.csv", "456.csv", "457.csv", "458.csv", "459.csv", "460.csv", "461.csv", "462.csv", "463.csv", "464.csv", "465.csv", "466.csv", "467.csv", "468.csv", "469.csv", "470.csv", "471.csv", "472.csv", "473.csv", "474.csv", "475.csv", "476.csv", "477.csv", "478.csv", "479.csv", "480.csv", "481.csv", "482.csv", "483.csv", "484.csv", "485.csv", "486.csv", "487.csv", "488.csv", "489.csv", "490.csv", "491.csv", "492.csv", "493.csv", "494.csv", "495.csv", "496.csv", "497.csv", "498.csv", "499.csv", "500.csv", "501.csv", "502.csv", "503.csv", "504.csv", "505.csv", "506.csv", "507.csv", "508.csv", "509.csv", "510.csv", "511.csv", "512.csv", "513.csv", "514.csv", "515.csv", "516.csv", "517.csv", "518.csv", "519.csv", "520.csv", "521.csv", "522.csv", "523.csv", "524.csv", "525.csv", "526.csv", "527.csv", "528.csv", "529.csv", "530.csv", "531.csv", "532.csv", "533.csv", "534.csv", "535.csv", "536.csv", "537.csv", "538.csv", "539.csv", "540.csv", "541.csv", "542.csv", "543.csv", "544.csv", "545.csv", "546.csv", "547.csv", "548.csv", "549.csv", "550.csv", "551.csv", "552.csv", "553.csv", "554.csv", "555.csv", "556.csv", "557.csv", "558.csv", "559.csv", "560.csv", "561.csv", "562.csv", "563.csv", "564.csv", "565.csv", "566.csv", "567.csv", "568.csv", "569.csv", "570.csv", "571.csv", "572.csv", "573.csv", "574.csv", "575.csv", "576.csv", "577.csv", "578.csv", "579.csv", "580.csv", "581.csv", "582.csv", "583.csv", "584.csv", "585.csv", "586.csv", "587.csv", "588.csv", "589.csv", "590.csv", "591.csv", "592.csv", "593.csv", "594.csv", "595.csv", "596.csv", "597.csv", "598.csv", "599.csv", "600.csv", "601.csv", "602.csv", "603.csv", "604.csv", "605.csv", "606.csv", "607.csv", "608.csv", "609.csv", "610.csv", "611.csv", "612.csv", "613.csv", "614.csv", "615.csv", "616.csv", "617.csv", "618.csv", "619.csv", "620.csv", "621.csv", "622.csv", "623.csv", "624.csv", "625.csv", "626.csv", "627.csv", "628.csv", "629.csv", "630.csv", "631.csv", "632.csv", "633.csv", "634.csv", "635.csv", "636.csv", "637.csv", "638.csv", "639.csv", "640.csv", "641.csv", "642.csv", "643.csv", "644.csv", "645.csv", "646.csv", "647.csv", "648.csv", "649.csv", "650.csv", "651.csv", "652.csv", "653.csv", "654.csv", "655.csv", "656.csv", "657.csv", "658.csv", "659.csv", "660.csv", "661.csv", "662.csv", "663.csv", "664.csv", "665.csv", "666.csv", "667.csv", "668.csv", "669.csv", "670.csv", "671.csv", "672.csv", "673.csv", "674.csv", "675.csv", "676.csv", "677.csv", "678.csv", "679.csv", "680.csv", "681.csv", "682.csv", "683.csv", "684.csv", "685.csv", "686.csv", "687.csv", "688.csv", "689.csv", "690.csv", "691.csv", "692.csv", "693.csv", "694.csv", "695.csv", "696.csv", "697.csv", "698.csv", "699.csv", "700.csv", "701.csv", "702.csv", "703.csv", "704.csv", "705.csv", "706.csv", "707.csv", "708.csv", "709.csv", "710.csv", "711.csv", "712.csv", "713.csv", "714.csv", "715.csv", "716.csv", "717.csv", "718.csv", "719.csv", "720.csv", "721.csv", "722.csv", "723.csv", "724.csv", "725.csv", "726.csv", "727.csv", "728.csv", "729.csv", "730.csv", "731.csv", "732.csv", "733.csv", "734.csv", "735.csv", "736.csv", "737.csv", "738.csv", "739.csv", "740.csv", "741.csv", "742.csv", "743.csv", "744.csv", "745.csv", "746.csv", "747.csv", "748.csv", "749.csv", "750.csv", "751.csv", "752.csv", "753.csv", "754.csv", "755.csv", "756.csv", "757.csv", "758.csv", "759.csv", "760.csv", "761.csv", "762.csv", "763.csv", "764.csv", "765.csv", "766.csv", "767.csv", "768.csv", "769.csv", "770.csv", "771.csv", "772.csv", "773.csv", "774.csv", "775.csv", "776.csv", "777.csv", "778.csv", "779.csv", "780.csv", "781.csv", "782.csv", "783.csv", "784.csv", "785.csv", "786.csv", "787.csv", "788.csv", "789.csv", "790.csv", "791.csv", "792.csv", "793.csv", "794.csv", "795.csv", "796.csv", "797.csv", "798.csv", "799.csv", "800.csv", "801.csv", "802.csv", "803.csv", "804.csv", "805.csv", "806.csv", "807.csv", "808.csv", "809.csv", "810.csv", "811.csv", "812.csv", "813.csv", "814.csv", "815.csv", "816.csv", "817.csv", "818.csv", "819.csv", "820.csv", "821.csv", "822.csv", "823.csv", "824.csv", "825.csv", "826.csv", "827.csv", "828.csv", "829.csv", "830.csv", "831.csv", "832.csv", "833.csv", "834.csv", "835.csv", "836.csv", "837.csv", "838.csv", "839.csv", "840.csv", "841.csv", "842.csv", "843.csv", "844.csv", "845.csv", "846.csv", "847.csv", "848.csv", "849.csv", "850.csv", "851.csv", "852.csv", "853.csv", "854.csv", "855.csv", "856.csv", "857.csv", "858.csv", "859.csv", "860.csv", "861.csv", "862.csv", "863.csv", "864.csv", "865.csv", "866.csv", "867.csv", "868.csv", "869.csv", "870.csv", "871.csv", "872.csv", "873.csv", "874.csv", "875.csv", "876.csv", "877.csv", "878.csv", "879.csv", "880.csv", "881.csv", "882.csv", "883.csv", "884.csv", "885.csv", "886.csv", "887.csv", "888.csv", "889.csv", "890.csv", "891.csv", "892.csv", "893.csv", "894.csv", "895.csv", "896.csv", "897.csv", "898.csv", "899.csv", "900.csv", "901.csv", "902.csv", "903.csv", "904.csv", "905.csv", "906.csv", "907.csv", "908.csv", "909.csv", "910.csv", "911.csv", "912.csv", "913.csv", "914.csv", "915.csv", "916.csv", "917.csv", "918.csv", "919.csv", "920.csv", "921.csv", "922.csv", "923.csv", "924.csv", "925.csv", "926.csv", "927.csv", "928.csv", "929.csv", "930.csv", "931.csv", "932.csv", "933.csv", "934.csv", "935.csv", "936.csv", "937.csv", "938.csv", "939.csv", "940.csv", "941.csv", "942.csv", "943.csv", "944.csv", "945.csv", "946.csv", "947.csv", "948.csv", "949.csv", "950.csv", "951.csv", "952.csv", "953.csv", "954.csv", "955.csv", "956.csv", "957.csv", "958.csv", "959.csv", "960.csv", "961.csv", "962.csv", "963.csv", "964.csv", "965.csv", "966.csv", "967.csv", "968.csv", "969.csv", "970.csv", "971.csv", "972.csv", "973.csv", "974.csv", "975.csv", "976.csv", "977.csv", "978.csv", "979.csv", "980.csv", "981.csv", "982.csv", "983.csv", "984.csv", "985.csv", "986.csv", "987.csv", "988.csv", "989.csv", "990.csv", "991.csv", "992.csv", "993.csv", "994.csv", "995.csv", "996.csv", "997.csv", "998.csv", "999.csv", "1000.csv", "1001.csv", "1002.csv", "1003.csv", "1004.csv", "1005.csv", "1006.csv", "1007.csv", "1008.csv", "1009.csv", "1010.csv", "1011.csv", "1012.csv", "1013.csv", "1014.csv", "1015.csv", "1016.csv", "1017.csv", "1018.csv", "1019.csv", "1020.csv", "1021.csv", "1022.csv", "1023.csv", "1024.csv", "1025.csv", "1026.csv", "1027.csv", "1028.csv", "1029.csv", "1030.csv", "1031.csv", "1032.csv", "1033.csv", "1034.csv", "1035.csv", "1036.csv", "1037.csv", "1038.csv", "1039.csv", "1040.csv", "1041.csv", "1042.csv", "1043.csv", "1044.csv", "1045.csv", "1046.csv", "1047.csv", "1048.csv", "1049.csv", "1050.csv", "1051.csv", "1052.csv", "1053.csv", "1054.csv", "1055.csv", "1056.csv", "1057.csv", "1058.csv", "1059.csv", "1060.csv", "1061.csv", "1062.csv", "1063.csv", "1064.csv", "1065.csv", "1066.csv", "1067.csv", "1068.csv", "1069.csv", "1070.csv", "1071.csv", "1072.csv", "1073.csv", "1074.csv", "1075.csv", "1076.csv", "1077.csv", "1078.csv", "1079.csv", "1080.csv", "1081.csv", "1082.csv", "1083.csv", "1084.csv", "1085.csv", "1086.csv", "1087.csv", "1088.csv", "1089.csv", "1090.csv", "1091.csv", "1092.csv", "1093.csv", "1094.csv", "1095.csv", "1096.csv", "1097.csv", "1098.csv", "1099.csv", "1100.csv", "1101.csv", "1102.csv", "1103.csv", "1104.csv", "1105.csv", "1106.csv", "1107.csv", "1108.csv", "1109.csv", "1110.csv", "1111.csv", "1112.csv", "1113.csv", "1114.csv", "1115.csv", "1116.csv", "1117.csv", "1118.csv", "1119.csv", "1120.csv", "1121.csv", "1122.csv", "1123.csv", "1124.csv", "1125.csv", "1126.csv", "1127.csv", "1128.csv", "1129.csv", "1130.csv", "1131.csv", "1132.csv", "1133.csv", "1134.csv", "1135.csv", "1136.csv", "1137.csv", "1138.csv", "1139.csv", "1140.csv", "1141.csv", "1142.csv", "1143.csv", "1144.csv", "1145.csv", "1146.csv", "1147.csv", "1148.csv", "1149.csv", "1150.csv", "1151.csv", "1152.csv", "1153.csv", "1154.csv", "1155.csv", "1156.csv", "1157.csv", "1158.csv", "1159.csv", "1160.csv", "1161.csv", "1162.csv", "1163.csv", "1164.csv", "1165.csv", "1166.csv", "1167.csv", "1168.csv", "1169.csv", "1170.csv", "1171.csv", "1172.csv", "1173.csv", "1174.csv", "1175.csv", "1176.csv", "1177.csv", "1178.csv", "1179.csv", "1180.csv", "1181.csv", "1182.csv", "1183.csv", "1184.csv", "1185.csv", "1186.csv", "1187.csv", "1188.csv", "1189.csv", "1190.csv", "1191.csv", "1192.csv", "1193.csv", "1194.csv", "1195.csv", "1196.csv", "1197.csv", "1198.csv", "1199.csv"]

    for renamedfile in range (0, 600):
        try:
            print listLoad[renamedfile]
            myFileNameLoad = SAVE_TO_DIRECTORY[directory] +'/' + listLoad[renamedfile]
            
            #this loops through your renamed files
            

            with open(myFileNameLoad, 'rb') as pageList:
                stateReader = csv.reader(pageList, delimiter=',', quotechar='|')
                #this is for the rows in your downloaded file
                start = 1
                end = 1000
                for row in itertools.islice(stateReader, start, end):
                    saveRow = ', '.join(row)
                    #this saves the row into the common csv file
                    saveFile = open(completeFile, 'a')
                    saveFile.write(saveRow)
                    saveFile.write("\n")
                    saveFile.close()
                print myFileNameLoad
                print "Work in progress..."
        except:
            pass


    print "Finished"
