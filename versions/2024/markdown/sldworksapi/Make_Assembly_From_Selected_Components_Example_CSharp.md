---
title: "Make Assembly from Selected Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Assembly_From_Selected_Components_Example_CSharp.htm"
---

# Make Assembly from Selected Components Example (C#)

This example shows how to create a new assembly using the selected components
of the active assembly.

//--------------------------------------------------------------------- // Preconditions: // 1. Open public_documents \samples\tutorial\motionstudies\valve_cam2.sldasm // 2. Ensure that the Save new components to external files check box // on the Tools > Options > Assemblies dialog is
selected. // Otherwise, the selected components are saved as virtual
components // and not as external files. // 3. Select valve<1> and valve_guide<1> components. // // Postconditions: // 1. Creates public_documents \samples\tutorial\motionstudies\MyTestValveAssembly.sldasm , // which is made up of the valve<1> and valve_guide<1> components. // 2. Replaces the valve<1> and valve_guide<1> components with // MyTestValveAssembly subassembly. // 3. Examine the FeatureManager design tree and // public_documents \samples\tutorial\motionstudies . // 4. Clear the S ave new components to external files check box // on the Tools > Options > Assemblies dialog if you
selected // it for this example. // // NOTE: Because the assembly is used elsewhere, do not save changes. //-----------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

using System.Diagnostics;

namespace MakeAssemblyFromSelectedComponents_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swModel = default(ModelDoc2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AssemblyDoc
swAssy = default(AssemblyDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
tmpPath = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
strCompModelname = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strCompModelname
= "MyTestValveAssembly.sldasm";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Save the new assembly in the same folder as the original assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}tmpPath
= swModel.GetPathName();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}tmpPath
= tmpPath.Substring(0, tmpPath.Length - 17);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(
tmpPath);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAssy
= (AssemblyDoc)swModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Create a new assembly using the selected components

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAssy.MakeAssemblyFromSelectedComponents(tmpPath
+ strCompModelname);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
