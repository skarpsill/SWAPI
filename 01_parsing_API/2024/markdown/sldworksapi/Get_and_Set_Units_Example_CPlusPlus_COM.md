---
title: "Get and Set Units Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Units_Example_CPlusPlus_COM.htm"
---

# Get and Set Units Example (C++ COM)

This example shows how to get the current unit
settings of the document and change them to inches. Be sure to import
swconst.tlb.

The method IModelDoc2::IGetUnits returns an
array, so this code must be used in an in-process DLL. Otherwise, use
the method IModelDoc2::GetUnits that returns a VARIANT.

GetAndSetUnits(ISldWorks* m_pSldWorks)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOC2
pModelDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve Model Document pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
S_OK != m_pSldWorks->get_IActiveDoc2(
&pModelDoc ) || pModelDoc == NULL )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}short
unitArray[5];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
hres = S_OK;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->IGetUnits(unitArray);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
message;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Create message string

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}message.Format(_T("Unit
Settings are:\n%d \t%d \t%d \t%d \t%d"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}unitArray[0],unitArray[1],unitArray[2],unitArray[3],unitArray[4]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Send message to the user

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AfxMessageBox
(message);kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
If units are not inches, change them to inches

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(unitArray[0] != swINCHES)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}short
denom = 16;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= pModelDoc->SetUnits(swINCHES,
swFRACTION, denom, unitArray[3], FALSE);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->Release();

}
