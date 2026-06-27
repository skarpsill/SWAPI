---
title: "Get Sketch Segment Constraints Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Segment_Constraints_Example_CPlusPlus_COM.htm"
---

# Get Sketch Segment Constraints Example (C++ COM)

This example shows how to get the constraints for the selected sketch
segment.

// -------------------------------------------------------------------

void APITestFunction()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANT_BOOLkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= VARIANT_FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nRetVal
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISelectionMgr>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IUnknown>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pUnk;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<ISketchSegment>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSkSeg;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nNumConstr
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTR*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pConstrArr
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
connect to SW

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->get_ISelectionManager(&pSelMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSelMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSelMgr->IGetSelectedObject5(1,
&pUnk);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pUnk);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSkSeg
= pUnk;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSkSeg);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSkSeg->IGetConstraintsCount(&nNumConstr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT
(nNumConstr > 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pConstrArr
= new BSTR[nNumConstr];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pConstrArr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(pConstrArr,
nNumConstr * sizeof(BSTR));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSkSeg->IGetConstraints(pConstrArr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pConstrArr[0]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < nNumConstr; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sConstrStr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sConstrStr.Attach(pConstrArr[i]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(sConstrStr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(_T("\n"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] pConstrArr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

} //void APITestFunction()

// -------------------------------------------------------------------
