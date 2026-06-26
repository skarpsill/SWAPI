---
title: "Combine Bodies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Combine_Bodies_Example_VBNET.htm"
---

# Combine Bodies Example (VB.NET)

This example shows how to combine bodies in a multibody part.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects two solid bodies.
' 3. Inserts a combine feature using the two selected
'    bodies.
' 4. Prints the type of combine feature to the Immediate
'    window.
' 5. Examine the Immediate window.
'
' NOTE: Because the part document is used elsewhere, do not
' save changes.
'--------------------------------------------------------------
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureMgr As FeatureManager
        Dim swFeature As Feature
        Dim swCombineBodiesFeatureData As CombineBodiesFeatureData
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, False, 2, Nothing, 0)
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 2, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.InsertCombineFeature(swBodyOperationType_e.SWBODYADD, Nothing, Nothing)

        swCombineBodiesFeatureData = swFeature.GetDefinition
        status = swCombineBodiesFeatureData.AccessSelections(swModel, Nothing)
        'swCombineBodiesOperationType_e:
        ' swCombineBodiesOperationAdd = 0
        ' swCombineBodiesOperationCommon = 2
        ' swCombineBodiesOperationSubract = 1
        Debug.Print("Type of combine feature: " & swCombineBodiesFeatureData.OperationType)
        swCombineBodiesFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
