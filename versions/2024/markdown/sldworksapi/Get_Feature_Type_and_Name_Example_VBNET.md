---
title: "Get Feature Type and Name Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Feature_Type_and_Name_Example_VBNET.htm"
---

# Get Feature Type and Name Example (VB.NET)

This example shows how to get the feature type and name of the selected feature for use with IModelDocExtension::SelectByID2.

```
'----------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
' 2. Expand any component in the FeatureManager design tree
'    and select one of its features.
'
' Postconditions:
' 1. Gets the selected feature's type and name.
' 2. Examine the Immediate window.
'
' NOTE: Because this assembly document is used elsewhere, do not save changes.
'----------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeat As Feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim featName As String, featType As String

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the selected feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeat = swSelMgr.GetSelectedObject6(1, -1)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}featType = ""
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}featName = ""

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the feature's type and name
        kadov_tag{{</spaces>}}featName = swFeat.GetNameForSelection(featType)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt.SelectByID2(featName, featType, 0, 0, 0, True, 0, Nothing, 0)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Print the feature's type and name
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' to the Immediate window
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Feature type: " & featType)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Feature name: " & featName)

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
