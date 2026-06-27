---
title: "Create Split Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Split-body_Feature_Example_VBNET.htm"
---

# Create Split Feature Example (VB.NET)

This example shows how to create a Split feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document that contains a body that is bisected by
 '    Top Plane.
 ' 2. Verify that c:\temp exists.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Split1.
 ' 2. Saves a split body to c:\temp\Body1.sldprt.
 ' 3. Inspect the Immediate window, FeatureManager design tree, graphics area,
 '    and c:\temp.
 '---------------------------------------------------------------------------
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swSelMgr As SelectionMgr
    Dim swModelDocExt As ModelDocExtension
    Dim swFeat As Feature
    Dim swFeatMgr As FeatureManager
    Dim swSplitBodyFeat As SplitBodyFeatureData
    Dim boolstatus As Boolean

    Sub main()

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        swFeatMgr = swModel.FeatureManager

        'Select the cutting tool
        boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

        'Get bodies resulting from the split operation
        Dim vResultingBodies(3) As Object
        vResultingBodies = swFeatMgr.PreSplitBody2

        swModel.ClearSelection2(True)

        Dim vBodyNames As Object
        Dim bodiesToMark(1) As Body2
        Dim bodyNames(1) As String
        Dim bodyOrigins(1) As Vertex

        'Set up the arrays for the post-split operation

        'Assign the origins of bodies to save; set to nothing to use default origins
        bodyOrigins(0) = Nothing
        bodyOrigins(1) = Nothing

        bodiesToMark(0) = vResultingBodies(0)
        bodiesToMark(1) = vResultingBodies(1)

        'Save the first body to a separate part document
        bodyNames(0) = "c:\temp\Body1.sldprt"
        'Do not save the second body
        bodyNames(1) = ""

        Dim preSplitBodies() As DispatchWrapper
        preSplitBodies = ObjectArrayToDispatchWrapperArray((bodiesToMark))
        vBodyNames = bodyNames
        Dim originsToUse() As DispatchWrapper
        originsToUse = ObjectArrayToDispatchWrapperArray((bodyOrigins))

        'Create the Split feature, consuming all split bodies
        swFeat = swFeatMgr.PostSplitBody2((preSplitBodies), True, (originsToUse), (vBodyNames), "")

        If (Not swFeat Is Nothing) Then
            Debug.Print("Split feature: " & swFeat.Name)
            swSplitBodyFeat = swFeat.GetDefinition
            Debug.Print("Bodies consumed? " & swSplitBodyFeat.Consume)
            Debug.Print(" ")
        End If

    End Sub

    Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()
        Dim ArraySize As Integer
        ArraySize = Objects.GetUpperBound(0)
        Dim d(ArraySize) As DispatchWrapper
        Dim ArrayIndex As Integer
        For ArrayIndex = 0 To ArraySize
            d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
        Next
        Return d

    End Function

    Public swApp As SldWorks

End Class
```
