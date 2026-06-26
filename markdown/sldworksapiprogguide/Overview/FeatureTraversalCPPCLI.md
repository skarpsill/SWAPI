---
title: "FeatureTraversalC++CLI"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/FeatureTraversalCPPCLI.htm"
---

# FeatureTraversalC++CLI

## FeatureTraversal.cpp Written in C++/CLI

// FeatureTraversal.cpp : main project file

// Traverses the FeatureManager design tree in the active
model document

#include "stdafx.h"

using namespace System;

// Add the SOLIDWORKS primary interop assemblies to
the reference

using namespace SolidWorks::Interop::sldworks;

using namespace SolidWorks::Interop::swconst;

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

IFeature^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeature;

IFeature^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSubFeature;

String^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strFeatureName;

String^kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strFeatureType;

swFeature = swModel->IFirstFeature();

while (swFeature) {

strFeatureName = swFeature->Name;

strFeatureType = swFeature->GetTypeName2();

swSubFeature = swFeature->IGetFirstSubFeature();

while (swSubFeature) {

strFeatureName = swSubFeature->Name;

strFeatureType = swSubFeature->GetTypeName2();

swSubFeature = swSubFeature->IGetNextSubFeature();

}

swFeature = swFeature->IGetNextFeature();

}

return(0);

}
