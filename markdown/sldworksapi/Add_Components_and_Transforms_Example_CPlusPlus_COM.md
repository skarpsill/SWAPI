---
title: "Add Components and Transforms Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Components_and_Transforms_Example_CPlusPlus_COM.htm"
---

# Add Components and Transforms Example (C++ COM)

This example shows how to use transforms when adding components.

// -------------------------------------------------------------------

void APITestFunction()

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nRetVal
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr
<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComQIPtr
<IAssemblyDoc>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pAssy;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nNumComp
= 2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sPartPath[2]
=

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_T("c:/samples/Part1.SLDPRT"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}_T("c:/samples/Part2.SLDPRT")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}};

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPCOMPONENTkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCompArr[2]
= { NULL, NULL};

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}doublekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dTransform[32]
=

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0.135786163522013,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-3.73411949685534E-02,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-2.04999999999997E-02,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-0.205037106918239,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-8.82610062893077E-03,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}-5.62499999999999E-02,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}};

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->get_IActiveDoc2(&pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModel);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pAssy
= pModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pAssy);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pAssy->IAddComponents2(&nNumComp,
sPartPath, dTransform, swCompArr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(swCompArr[0]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(swCompArr[1]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= swCompArr[0]->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= swCompArr[1]->Release();

}

// -------------------------------------------------------------------
