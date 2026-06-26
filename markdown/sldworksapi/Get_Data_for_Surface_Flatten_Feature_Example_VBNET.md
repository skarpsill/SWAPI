---
title: "Get Data for Surface-flatten Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm"
---

# Get Data for Surface-flatten Feature Example (VB.NET)

This example shows how to insert a surface-flatten feature and get its data.

```
'-------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Inserts a surface-flatten feature.
' 3. Gets surface-flatten feature data.
' 4. Examine the graphics area and FeatureManager design
'    tree.
'
' NOTE: Because this part is used elsewhere, do not save
' changes.
'--------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim swSurfaceFlattenFeatureData As SurfaceFlattenFeatureData
        Dim swEdge As Edge
        Dim status As Boolean
        Dim warnings As Integer
        Dim errors As Integer
        Dim fileName As String
        Dim edges As Object
        Dim nbrTearEdges As Integer
        Dim i As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\Hemisphere.SLDPRT"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        ' Select face, vertex, and curves for surface-flatten feature
        status = swModelDocExt.SelectByID2("", "FACE", 0.00546207138008786, -0.0373996629648742, 0.0130049636270216, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "VERTEX", 0, -0.0400014251170795, -0.00054185036618795, True, 16, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.011047389592717, -0.00000623453597697887, 0.0382739927527045, True, 8, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0108290857690036, -0.0262767618508641, 0.0280128973987478, True, 8, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.00907918330954303, 0.0286363967873063, 0.0262553195430037, True, 8, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0157595492108076, 0.0240950142317162, -0.0272880335909787, True, 8, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0143808110794609, -0.0281074423709366, -0.0240578702886196, True, 8, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.01886657492451, 0.0000248139106812095, -0.035004838468241, True, 8, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0140143161426676, -0.0374399859522778, 0.000123652313243445, True, 8, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0164192327552536, 0.0363245554251959, -0.0000958561062339106, True, 8, Nothing, 0)

        ' Create surface-flatten feature
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.InsertFlattenSurface2(8, True)

        ' Get some surface-flatten feature data
        swSurfaceFlattenFeatureData = swFeature.GetDefinition
        swSurfaceFlattenFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Feature = " & swFeature.Name)
        Debug.Print("   Accuracy of flattened triangle mesh =  " & swSurfaceFlattenFeatureData.AccuracyFactor)
        Debug.Print("   Keep internal control curves? " & swSurfaceFlattenFeatureData.KeepInternalControlCurves)
        If swSurfaceFlattenFeatureData.ShouldMakeTears = True Then
            Debug.Print("   Tear edges: ")
            edges = swSurfaceFlattenFeatureData.TearEdges
            nbrTearEdges = UBound(edges) + 1
            Debug.Print("      Number of tear edges: " & nbrTearEdges)
            For i = 0 To UBound(edges)
                swEdge = edges(i)
                Dim swSelMgr As SelectionMgr
                swSelMgr = swModel.SelectionManager
                status = swSelMgr.AddSelectionListObject(swEdge, Nothing)
                Debug.Print("            Type of object (51 = swSelREFEDGES): " & swSelMgr.GetSelectedObjectType3(1, -1))
            Next i
        End If
        swSurfaceFlattenFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
