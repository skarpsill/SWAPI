---
title: "Deselect Every Other Selected Object Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Deselect_Every_Other_Selected_Object_Example_CPlusPlus_COM.htm"
---

# Deselect Every Other Selected Object Example (C++ COM)

This example shows how to deselect every other object.

// -------------------------------------------------------------------

void APITestFunction()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= FALSE;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nRetVal
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISelectionMgr>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDeSelectArr
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDeSelectCount
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nOldSelCount
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nNewSelCount
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS application

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
= pSelMgr->GetSelectedObjectCount(&nOldSelCount);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(nOldSelCount
> 1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDeSelectCount
= floor(nOldSelCount / 2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDeSelectArr
= new long[nDeSelectCount];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(nDeSelectArr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(nDeSelectArr,
nDeSelectCount * sizeof(long));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < nDeSelectCount; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Deselect every other item

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Memory array is 0-based, but SelectionMgr array is 1-based

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDeSelectArr[i]
= 2 * i + 1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSelMgr->IDeSelect(nDeSelectCount,
nDeSelectArr, &bRet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(bRet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSelMgr->GetSelectedObjectCount(&nNewSelCount);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(nNewSelCount
== nOldSelCount - nDeSelectCount);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] nDeSelectArr;

}

// -------------------------------------------------------------------
