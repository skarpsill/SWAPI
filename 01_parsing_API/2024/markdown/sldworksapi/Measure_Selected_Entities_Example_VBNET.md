---
title: "Measure Selected Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Measure_Selected_Entities_Example_VBNET.htm"
---

# Measure Selected Entities Example (VB.NET)

This example shows how to use the measure tool.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document as read only.
' 2. Selects two faces and measures them.
' 3. Examine the Immediate window.
'-----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swMeasure As Measure
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\dimxpert\coupling_auto_geo.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", -0.00382117299216134, -0.0032246917626253, -0.00153854043344381, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0.00547600669648318, 0.00252191841298099, 0.0050000000000523, True, 0, Nothing, 0)
        swMeasure = swModelDocExt.CreateMeasure
        'Can set this to 0
        ' 0 = center to center
        ' 1 = minimum distance
        ' 2 = maximum distance
        swMeasure.ArcOption = 0

        status = swMeasure.Calculate(Nothing)
        If (status) Then
            If (Not (swMeasure.Length = -1)) Then
                Debug.Print("Length: " & swMeasure.Length)
            End If
            If (Not (swMeasure.Area = -1)) Then
                Debug.Print("Area: " & swMeasure.Area)
            End If
            If (Not (swMeasure.ArcLength = -1)) Then
                Debug.Print("Arc length: " & swMeasure.ArcLength)
            End If
            If (Not (swMeasure.ChordLength = -1)) Then
                Debug.Print("Chord length: " & swMeasure.ChordLength)
            End If
            If (Not (swMeasure.Diameter = -1)) Then
                Debug.Print("Diameter: " & swMeasure.Diameter)
            End If
            If (Not (swMeasure.Radius = -1)) Then
                Debug.Print("Radius: " & swMeasure.Radius)
            End If
            If (Not (swMeasure.Perimeter = -1)) Then
                Debug.Print("Perimeter: " & swMeasure.Perimeter)
            End If
            If (Not (swMeasure.X = -1)) Then
                Debug.Print("X coordinate: " & swMeasure.X)
            End If
            If (Not (swMeasure.Y = -1)) Then
                Debug.Print("Y coordinate: " & swMeasure.Y)
            End If
            If (Not (swMeasure.Z = -1)) Then
                Debug.Print("Z coordinate: " & swMeasure.Z)
            End If
            If (Not (swMeasure.DeltaX = -1)) Then
                Debug.Print("DeltaX: " & swMeasure.DeltaX)
            End If
            If (Not (swMeasure.DeltaY = -1)) Then
                Debug.Print("DeltaY: " & swMeasure.DeltaY)
            End If
            If (Not (swMeasure.DeltaZ = -1)) Then
                Debug.Print("DeltaZ: " & swMeasure.DeltaZ)
            End If
            If (Not (swMeasure.Angle = -1)) Then
                Debug.Print("Angle: " & swMeasure.Angle)
            End If
            If (Not (swMeasure.CenterDistance = -1)) Then
                Debug.Print("Center distance: " & swMeasure.CenterDistance)
            End If
            If (Not (swMeasure.NormalDistance = -1)) Then
                Debug.Print("Normal distance: " & swMeasure.NormalDistance)
            End If
            If (Not (swMeasure.Distance = -1)) Then
                Debug.Print("Distance: " & swMeasure.Distance)
            End If
            If (Not (swMeasure.TotalLength = -1)) Then
                Debug.Print("Total length: " & swMeasure.TotalLength)
            End If
            If (Not (swMeasure.TotalArea = -1)) Then
                Debug.Print("Total area: " & swMeasure.TotalArea)
            End If
            If (swMeasure.IsParallel) Then
                Debug.Print("Is parallel: " & swMeasure.IsParallel)
            End If
            If (swMeasure.IsIntersect) Then
                Debug.Print("Is intersect: " & swMeasure.IsIntersect)
            End If
            If (swMeasure.IsPerpendicular) Then
                Debug.Print("Is perpendicular: " & swMeasure.IsPerpendicular)
            End If
            If (Not (swMeasure.Projection = -1)) Then
                Debug.Print("Projection: " & swMeasure.Projection)
            End If
            If (Not (swMeasure.Normal = -1)) Then
                Debug.Print("Normal: " & swMeasure.Normal)
            End If
            If (Not (swMeasure.SpericalCenterDistance = -1)) Then
                Debug.Print("Spherical center distance: " & swMeasure.SpericalCenterDistance)
            End If
            If (swMeasure.IsConcentricSpheres) Then
                Debug.Print("Are concentric spheres: " & swMeasure.IsConcentricSpheres)
            End If
        Else
            Debug.Print("Invalid combination of selected entities.")
        End If
        swModel.ClearSelection2(True)
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
