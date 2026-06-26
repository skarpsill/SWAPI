---
title: "SelectionManagerC++"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SelectionManagerCPP.htm"
---

# SelectionManagerC++

## SelectionManager.cpp Written in C++

// SelectionManager.cpp : Defines the entry point for
the console application

// Gets the selected objects in the active model document

#include "stdafx.h"

// Add the path to the SOLIDWORKS type libraries to
the "Additional Include Directories".

#import "sldworks.tlb" raw_interfaces_only,
raw_native_types, no_namespace, named_guidskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
SOLIDWORKS type library

#import "swconst.tlb" raw_interfaces_only,
raw_native_types, no_namespace, named_guidskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
SOLIDWORKS constants type library

int _tmain(int argc, _TCHAR* argv[])

{

// Initialize COM

// Do this before using ATL smart pointers
so COM is available

CoInitialize(NULL);

// Use a block so the smart pointers are
destructed when the scope of this block is left

{

// Use ATL smart pointers

CComPtr<ISldWorks>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp;

if(swApp.CoCreateInstance(__uuidof(SldWorks),
NULL, CLSCTX_LOCAL_SERVER) != S_OK) {

return(0);kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

}

swApp->put_UserControl(VARIANT_TRUE);

swApp->put_Visible(VARIANT_TRUE);

CComPtr<IModelDoc2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel;

swApp->get_IActiveDoc2(&swModel);

if (! swModel) {

return(0);

}

CComBSTRkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strModelTitle;

longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDocumentType;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}// swDocumentTypes_e

swModel->GetTitle(&strModelTitle);

swModel->GetType(&nDocumentType);

CComPtr<ISelectionMgr>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelectionManager;

longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lNumSelections;

longkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nSelectionType;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
swSelectType_e

CComPtr<IDispatch>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelectedObject;

CComPtr<IFace2>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace;

CComPtr<IEdge>kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEdge;

swModel->get_ISelectionManager(&swSelectionManager);

swSelectionManager->GetSelectedObjectCount2(-1,
&lNumSelections);

for (int i = 1; i <= lNumSelections;
i++) {

swSelectionManager->GetSelectedObject6(i,
-1, &swSelectedObject);

swSelectionManager->GetSelectedObjectType3(i,
-1, &nSelectionType);

switch (nSelectionType) {

case swSelectType_e::swSelFACES:

swSelectedObject.QueryInterface(&swFace);

break;

case swSelectType_e::swSelEDGES:

swSelectedObject.QueryInterface(&swEdge);

break;

}

}

}

// ATL smart pointers are destructed so
all COM objects you held on to are released

// Now you can safely shut down COM as you
do not need it any longer

// Stop COM

CoUninitialize();

return(0);

}
