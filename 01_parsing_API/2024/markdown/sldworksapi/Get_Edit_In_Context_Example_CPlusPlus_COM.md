---
title: "Detecting In-Context Edit Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edit_In_Context_Example_CPlusPlus_COM.htm"
---

# Detecting In-Context Edit Example (C++ COM)

## Detect In-Context Edit Example (C++ COM)

This example shows how to trap an swAssemblyBeginInContextEditNotify
event and examine the document being edited in an assembly.

1. Create a new C++ COM add-in with the Visual Studio.NET COM AppWizard.
2. SelectAssembly
  Eventson theSwOptionspage.
3. After the wizard finishes generating code, add
  this code to the specified files.

SINK_ENTRY_EX(ID_ASSEMBLY_EVENTS, __uuidof(DAssemblyDocEvents),
swAssemblyBeginInContextEditNotify,OnAssemblyBeginInContextEditNotify)

STDMETHOD(OnAssemblyBeginInContextEditNotify)(LPDISPATCH
newDoc, long docType); //

next to
the other SINK_ENTRY_EX and STDMETHOD Declarations

STDMETHODIMP CSwDocument::OnAssemblyBeginInContextEditNotify(LPDISPATCH
newDoc, long docType)

{

ATLTRACE("\tCCSwDocument::OnAssemblyBeginInContextEditNotify
called\n");

CComPtr<IModelDoc2> swModel;

iSwApp->get_IActiveDoc2(&swModel);

CComPtr<IModelDoc2> swNewModel;

newDoc->QueryInterface(__uuidof(IModelDoc2),
reinterpret_cast<void**>(&swNewModel));

CComBSTR ContextName;

CComBSTR MainName;

swNewModel->GetTitle(&ContextName);

swModel->GetTitle(&MainName);

CComBSTR message;

message.Append(OLESTR("Main Assembly:
"));

message.Append(MainName);

message.Append(OLESTR("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Component:
"));

message.Append(ContextName);

long res;

iSwApp->SendMsgToUser2(message,0,0,&res);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

return S_OK;

}

1. After loading the add-in, open an assembly, right-click
  a component, and selectEdit PartorEdit Subassembly. The new method
  OnAssemblyBeginInContextEditNotify that you implemented should be called.
