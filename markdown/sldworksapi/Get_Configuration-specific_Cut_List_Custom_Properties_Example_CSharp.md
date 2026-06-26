---
title: "Get Configuration-specific Cut List Custom Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Configuration-specific_Cut_List_Custom_Properties_Example_CSharp.htm"
---

# Get Configuration-specific Cut List Custom Properties Example (C#)

This example shows how to get configuration-specific cut list custom
properties.

//
===========================================================

// Preconditions:

// 1. Open a part that
has one or more configuration-specific cut lists with custom properties.

// (Or ask SOLIDWORKS API Support to send you the models that work
with this ICutListItem sample code.)

// 2. Open an
Immediate/Output window.

//

// Postconditions:
Inspect all the configurations' cut lists' custom properties in the
Immediate/Output window.

//
=============================================================

usingSystem;

usingSystem.Collections.Generic;

usingSystem.Linq;

usingSystem.Text;

usingSystem.Threading.Tasks;

usingSystem.Windows;

usingSystem.Windows.Forms;

usingSolidWorks.Interop.sldworks;

usingSolidWorks.Interop.swconst;

usingSystem.Diagnostics;

namespaceConfigSpecCutListCustomProps_CSharp

{

publicpartialclassSolidWorksMacro

{

ModelDoc2 swModel;

string[] vConfigNameArr;

stringvConfigName;

object[] cutlistobj;

CutListItem[] vcutlistItems;

CutListItem vcutlistItem;

CutListItem cutlistItem;

CustomPropertyManager cusPropMgr;

Configuration config;

intlRetVal;

objectvPropNames;

objectvPropTypes;

objectvPropValues;

objectresolved;

objectlinkProp;

inti;

intj;

stringpropName;

publicvoidMain()

{

swModel = (ModelDoc2)swApp. ActiveDoc ;

vConfigNameArr = (string[])swModel. GetConfigurationNames ();

foreach(var vConfigNameinvConfigNameArr)

{

Debug.Print("Configuration:
"+ vConfigName);

config = (Configuration)swModel. GetConfigurationByName (vConfigName);

cutlistobj = (object[])config. GetCutListItems ();

intn;

for(n=0; n <
cutlistobj.Length; n++)

{

vcutlistItem = (CutListItem)cutlistobj[n];

Debug.Print("Cut
list item #"+ n +" custom properties:");

cusPropMgr = vcutlistItem. CustomPropertyManager ;

lRetVal = cusPropMgr. GetAll3 (refvPropNames,refvPropTypes,refvPropValues,refresolved,reflinkProp);

object[]
propValues = (object[])vPropValues;

string[]
propNames = (string[])vPropNames;

for(j = 0; j < lRetVal; j++)

{

Debug.Print("
"+ propNames[j] +" "+ propValues[j]);

}

i = i + 1;

}

}

}

// The SldWorks swApp variable
is pre-assigned for you.

publicSldWorks swApp;

}

}
