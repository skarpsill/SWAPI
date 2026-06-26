---
title: "SelectionManagerC++CLI"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/SelectionManagerCPPCLI.htm"
---

# SelectionManagerC++CLI

/

## SelectionManager.cpp Written in C++/CLI

// SelectionManager.cpp : main project file

// Gets the selected objects in the active model document

#include "stdafx.h"

using namespace System;

// Add the SOLIDWORKS pPrimary interop assemblies to
the references

using namespace SOLIDWORKS::Interop::sldworks;

using namespace SOLIDWORKS::Interop::swconst;

int main(array<System::String ^> ^args)

{

ISldWorks^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp;

swApp = gcnew SldWorksClass;

if (! swApp) {

return(0);

}

swApp->UserControl = true;

swApp->Visible = true;

IModelDoc2^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel;

swModel = swApp->IActiveDoc2;

if (! swModel) {

return(0);

}

String^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strModelTitle;

swDocumentTypes_ekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nDocumentType;

strModelTitle = swModel->GetTitle();

nDocumentType = (swDocumentTypes_e)swModel->GetType();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

ISelectionMgr^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelectionManager;

swSelectType_ekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nSelectionType;

Object^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelectedObject;

IFace2^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace;

IEdge^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEdge;

swSelectionManager = swModel->ISelectionManager;

for (int i = 1; i <= swSelectionManager->GetSelectedObjectCount2(-1);
i++) {

swSelectedObject = swSelectionManager->GetSelectedObject6(i,
-1);

nSelectionType = (swSelectType_e)swSelectionManager->GetSelectedObjectType3(i,
-1);

switch (nSelectionType) {

case swSelectType_e::swSelFACES:

swFace =kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(Face2^)swSelectedObject;

break;

case swSelectType_e::swSelEDGES:

swEdge = (Edge^)swSelectedObject;

break;

}

}

return(0);

}
