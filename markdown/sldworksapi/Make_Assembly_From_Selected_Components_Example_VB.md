---
title: "Make Assembly From Selected Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Assembly_From_Selected_Components_Example_VB.htm"
---

# Make Assembly From Selected Components Example (VBA)

This example shows how to create a new assembly using the selected components
of the active assembly.

```vb
 '---------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\motionstudies\valve_cam2.sldasm
 ' 2. Ensure that the Save new components to external files check box
 '    on the Tools > Options > Assemblies dialog is selected.
 '    Otherwise, the selected components are saved as virtual components
 '    and not as external files.
 ' 3. Select valve<1> and valve_guide<1> components.
 '
 ' Postconditions:
 ' 1. Creates public_documents\samples\tutorial\motionstudies\MyTestValveAssembly.sldasm,
 '    which is made up of the valve<1> and valve_guide<1> components.
 ' 2. Replaces the valve<1> and valve_guide<1> components with
 '    MyTestValveAssembly subassembly.
 ' 3. Examine the FeatureManager design tree and
 '    public_documents\samples\tutorial\motionstudies.
 ' 4. Clear the Save new components to external files check box
 '    on the Tools > Options > Assemblies dialog if you selected
 '    it for this example.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '-----------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssy As SldWorks.AssemblyDoc
Dim tmpPath As String
Dim boolstat As Boolean

Sub main()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstat = True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim strCompModelname As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strCompModelname = "MyTestValveAssembly.sldasm"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Save the new assembly in the same folder as the original assembly
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}tmpPath = Left(swModel.GetPathName, InStrRev(swModel.GetPathName, "\"))

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swAssy = swModel
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Create a new assembly using the selected components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swAssy.MakeAssemblyFromSelectedComponents (tmpPath + strCompModelname)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
```
