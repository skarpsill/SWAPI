---
title: "Insert Macro Feature Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Macro_Feature_Example_CPlusPlus_COM.htm"
---

# Insert Macro Feature Example (C++ COM)

This example shows how to insert a macro feature.

//-------------------------------------------

void APITestFunction()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IPartDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPart;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IBody2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pBody;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IFeatureManager>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFeatMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IFeature>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pFeat;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[9];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= VARIANT_FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPart
= pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pPart);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pPart->IBodyObject2(&pBody);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pBody);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->get_FeatureManager(&pFeatMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pFeatMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[0]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[1]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[2]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[3]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[4]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[5]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[6]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[7]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods[8]
= _T("");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pFeatMgr->IInsertMacroFeature(

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTR(_T("CeTestMacro")),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTR(_T("Sample.SimpleExtrude")),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sMacroMethods,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NULL,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NULL,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NULL,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pBody,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMacroFeatureSecurityByDefault,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}&pFeat);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pFeat);

} //void APITestFunction()

// -------------------------------------------------------------------
