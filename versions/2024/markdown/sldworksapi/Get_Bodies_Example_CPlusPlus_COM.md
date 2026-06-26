---
title: "Get Bodies Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bodies_Example_CPlusPlus_COM.htm"
---

# Get Bodies Example (C++ COM)

This example shows how to get the bodies in a part document.

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IPartDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPart;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VARIANTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodyArr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModel->ClearSelection2(VARIANT_TRUE);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pPart
= pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pPart);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pPart->GetBodies2(swSolidBody,
VARIANT_TRUE, &vBodyArr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(NULL
!= vBodyArr.pparray);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Process bodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SAFEARRAY*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}psaBody
= V_ARRAY(&vBodyArr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPDISPATCH*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pBodyDispArray
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nBodyHighIndex
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nBodyCount
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= SafeArrayAccessData(psaBody, (void **) &pBodyDispArray);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(S_OK
== hr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(NULL
!= pBodyDispArray);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get index number of highest array element

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
The array range is from 0 to highIndex

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= SafeArrayGetUBound(psaBody, 1, &nBodyHighIndex);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(S_OK
== hr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Actual number of array elements is nBodyHighIndex + 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nBodyCount
= nBodyHighIndex + 1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Process each body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < nBodyCount; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IBody2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pBody;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Calls AddRef() on IDispatch ---> refcount = 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pBody
= pBodyDispArray[i];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pBody);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pBody->Select(VARIANT_TRUE,
0, &bRet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(bRet);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
After this call ---> refcount = 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
When it goes out of scope ---> refcount = 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pBody.Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Unaccess & destroy the component SafeArray

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= SafeArrayUnaccessData(psaBody);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= SafeArrayDestroy(psaBody);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

} //void APITestFunction()

// -------------------------------------------------------------------
