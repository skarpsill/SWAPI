---
title: "Document Version History Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Document_Version_History_Example_CPlusPlus_COM.htm"
---

# Document Version History Example (C++ COM)

## Obtain Version History Example (C++ COM)

This example shows how to obtain a version
history of a file. IModelDoc2::IVersionHistory returns an array, so this
code must be used in an in-process DLL.

DocumentVersionHistory(ISldWorks* m_pSldWorks)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSTR*
versionHistStrings = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOC2
pModelDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
hres= S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= m_pSldWorks->get_IActiveDoc2(&pModelDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(hres != S_OK || pModelDoc == NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
versHistCount = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->IGetVersionHistoryCount(&versHistCount);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(hres != S_OK || versHistCount == 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}versionHistStrings
= new BSTR[versHistCount];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->IVersionHistory(versionHistStrings);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(hres != S_OK || versionHistStrings == NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] versionHistStrings;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
For each version found

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(int ii = 0;ii < versHistCount;ii++)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
tempstr2(versionHistStrings[ii]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AfxMessageBox
(tempstr2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SysFreeString(
versionHistStrings[ii]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
default destructor

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] versionHistStrings;

}
