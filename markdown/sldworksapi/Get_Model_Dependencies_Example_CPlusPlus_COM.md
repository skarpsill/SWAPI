---
title: "Get Model Dependencies Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Dependencies_Example_CPlusPlus_COM.htm"
---

# Get Model Dependencies Example (C++ COM)

This example shows how to get the names of the dependencies for a model.

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nNumDepend
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTR*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}psDepends
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS application

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->get_IActiveDoc2(&pModelDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pModelDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModelDoc->IGetNumDependencies(VARIANT_TRUE,
VARIANT_TRUE, &nNumDepend);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(nNumDepend
> 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}psDepends
= new BSTR[nNumDepend];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(psDepends);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ZeroMemory(psDepends,
nNumDepend * sizeof(BSTR));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModelDoc->IGetDependencies2(VARIANT_TRUE,
VARIANT_TRUE, VARIANT_FALSE, psDepends);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(psDepends);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i < nNumDepend / 2; i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sDepend1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sDepend2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sOutputStr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sDepend1.Attach(psDepends[2
* i + 0]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sDepend2.Attach(psDepends[2
* i + 1]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sOutputStr
= sDepend1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sOutputStr
+= CComBSTR(_T(" --> "));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sOutputStr
+= sDepend2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sOutputStr
+= CComBSTR(_T("\n"));

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OutputDebugString(sOutputStr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] psDepends;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

} //void APITestFunction()

// -------------------------------------------------------------------
