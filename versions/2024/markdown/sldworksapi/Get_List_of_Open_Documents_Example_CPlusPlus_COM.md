---
title: "Get List of Open Documents Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_List_of_Open_Documents_Example_CPlusPlus_COM.htm"
---

# Get List of Open Documents Example (C++ COM)

This example shows how to get a list of the currently open SOLIDWORKS
documents.

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr<IEnumDocuments2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pEnumDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nFetched
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComPtr<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= -1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Connect to SOLIDWORKS application

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSldWorks
= TheApplication->GetSWApp();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pSldWorks);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pSldWorks->EnumDocuments2(&pEnumDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASSERT(pEnumDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pEnumDoc->Reset();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}do

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sPathName;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Reset before reuse

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Could also check HRESULT or nFetched

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pEnumDoc->Next(1, &pModelDoc,
&nFetched);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(pModelDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Debugging only

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hr
= pModelDoc->GetPathName(&sPathName);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}
while (pModelDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

} //void APITestFunction()

// -------------------------------------------------------------------
