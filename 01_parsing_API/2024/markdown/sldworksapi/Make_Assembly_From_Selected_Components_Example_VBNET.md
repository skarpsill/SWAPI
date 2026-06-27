---
title: "Make Assembly From Selected Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Assembly_From_Selected_Components_Example_VBNET.htm"
---

# Make Assembly From Selected Components Example (VB.NET)

This example shows how to make a new assembly using the selected components
of the active assembly.

'--------------------------------------------------------------------- ' Preconditions: ' 1. Open public_documents \samples\tutorial\motionstudies\valve_cam2.sldasm ' 2. Ensure that the Save new components to external files check box ' on the Tools > Options > Assemblies dialog is
selected. ' Otherwise, the selected components are saved as virtual
components ' and not as external files. ' 3. Select valve<1> and valve_guide<1> components. ' ' Postconditions: ' 1. Creates public_documents \samples\tutorial\motionstudies\MyTestValveAssembly.sldasm , ' which is made up of the valve<1> and valve_guide<1> components. ' 2. Replaces the valve<1> and valve_guide<1> components with ' MyTestValveAssembly subassembly. ' 3. Examine the FeatureManager design tree and ' public_documents \samples\tutorial\motionstudies . ' 4. Clear the S ave new components to external files check box ' on the Tools > Options > Assemblies dialog if you
selected ' it for this example. ' ' NOTE: Because the assembly is used elsewhere, do not save changes. '-----------------------------------------------------------------------

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAssy As AssemblyDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim tmpPath As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstat As Boolean

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstat = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim strCompModelname As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strCompModelname = "MyTestValveAssembly.sldasm"

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Save the new assembly in the same folder as the original assembly
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}tmpPath = Left(swModel.GetPathName, InStrRev(swModel.GetPathName, "\"))

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssy = swModel

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create a new assembly using the selected components
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssy.MakeAssemblyFromSelectedComponents(tmpPath + strCompModelname)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
