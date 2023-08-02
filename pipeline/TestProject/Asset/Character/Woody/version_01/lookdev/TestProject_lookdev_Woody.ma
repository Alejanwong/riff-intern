//Maya ASCII 2020 scene
//Name: TestProject_lookdev_Woody.ma
//Last modified: Thu, Jul 27, 2023 08:41:12 AM
//Codeset: 1252
requires maya "2020";
requires -nodeType "aiStandardSurface" "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19045)\n";
fileInfo "UUID" "39F44DC1-45B6-4286-6D9C-3DBAFD73C731";
createNode aiStandardSurface -n "main_lookdev";
	rename -uid "4448A0F8-4F2B-5154-7DD0-14A238DCBD5E";
	addAttr -ci true -sn "model" -ln "model" -dt "string";
	addAttr -ci true -sn "anim" -ln "anim" -dt "string";
	setAttr ".base_color" -type "float3" 0 0.84614992 1 ;
	setAttr ".model" -type "string" "X:/pipeline/TestProject/Asset/Character/Woody/version_01/model/TestProject_model_Woody.ma";
	setAttr ".anim" -type "string" "X:/pipeline/TestProject/Asset/Character/Woody/version_01/anim/TestProject_anim_Woody.ma";
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 3 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 6 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "arnold";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "main_lookdev.msg" ":defaultShaderList1.s" -na;
// End of TestProject_lookdev_Woody.ma
