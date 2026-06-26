---
title: "Measure Selected Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Measure_Selected_Entities_Example_VB.htm"
---

# Measure Selected Entities Example (VBA)

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
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMeasure As SldWorks.Measure
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\dimxpert\coupling_auto_geo.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", -3.82117299216134E-03, -3.2246917626253E-03, -1.53854043344381E-03, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 5.47600669648318E-03, 2.52191841298099E-03, 5.0000000000523E-03, True, 0, Nothing, 0)
```

```
    Set swMeasure = swModelDocExt.CreateMeasure
    'Can set this to 0
    ' 0 = center to center
    ' 1 = minimum distance
    ' 2 = maximum distance
    swMeasure.ArcOption = 0
```

```
    status = swMeasure.Calculate(Nothing)
    If (status) Then
```

```
        If (Not (swMeasure.Length = -1)) Then
            Debug.Print "Length: " & swMeasure.Length
        End If
```

```
        If (Not (swMeasure.Area = -1)) Then
           Debug.Print "Area: " & swMeasure.Area
        End If
```

```
        If (Not (swMeasure.ArcLength = -1)) Then
            Debug.Print "Arc length: " & swMeasure.ArcLength
        End If
```

```
        If (Not (swMeasure.ChordLength = -1)) Then
           Debug.Print "Chord length: " & swMeasure.ChordLength
        End If
```

```
        If (Not (swMeasure.Diameter = -1)) Then
           Debug.Print "Diameter: " & swMeasure.Diameter
        End If
```

```
        If (Not (swMeasure.Radius = -1)) Then
            Debug.Print "Radius: " & swMeasure.Radius
        End If
```

```
        If (Not (swMeasure.Perimeter = -1)) Then
            Debug.Print "Perimeter: " & swMeasure.Perimeter
        End If
```

```
        If (Not (swMeasure.X = -1)) Then
            Debug.Print "X coordinate: " & swMeasure.X
        End If
```

```
        If (Not (swMeasure.Y = -1)) Then
            Debug.Print "Y coordinate: " & swMeasure.Y
        End If
```

```
        If (Not (swMeasure.Z = -1)) Then
            Debug.Print "Z coordinate: " & swMeasure.Z
        End If
```

```
        If (Not (swMeasure.DeltaX = -1)) Then
            Debug.Print "DeltaX: " & swMeasure.DeltaX
        End If
```

```
        If (Not (swMeasure.DeltaY = -1)) Then
            Debug.Print "DeltaY: " & swMeasure.DeltaY
        End If
```

```
        If (Not (swMeasure.DeltaZ = -1)) Then
            Debug.Print "DeltaZ: " & swMeasure.DeltaZ
        End If
```

```
        If (Not (swMeasure.Angle = -1)) Then
            Debug.Print "Angle: " & swMeasure.Angle
        End If
```

```
        If (Not (swMeasure.CenterDistance = -1)) Then
            Debug.Print "Center distance: " & swMeasure.CenterDistance
        End If
```

```
        If (Not (swMeasure.NormalDistance = -1)) Then
            Debug.Print "Normal distance: " & swMeasure.NormalDistance
        End If
```

```
        If (Not (swMeasure.Distance = -1)) Then
            Debug.Print "Distance: " & swMeasure.Distance
        End If
```

```
        If (Not (swMeasure.TotalLength = -1)) Then
            Debug.Print "Total length: " & swMeasure.TotalLength
        End If
```

```
        If (Not (swMeasure.TotalArea = -1)) Then
            Debug.Print "Total area: " & swMeasure.TotalArea
        End If
```

```
        If (swMeasure.IsParallel) Then
            Debug.Print "Is parallel: " & swMeasure.IsParallel
        End If
```

```
        If (swMeasure.IsIntersect) Then
            Debug.Print "Is intersect: " & swMeasure.IsIntersect
        End If
```

```
        If (swMeasure.IsPerpendicular) Then
            Debug.Print "Is perpendicular: " & swMeasure.IsPerpendicular
        End If
```

```
        If (Not (swMeasure.Projection = -1)) Then
            Debug.Print "Projection: " & swMeasure.Projection
        End If
```

```
        If (Not (swMeasure.Normal = -1)) Then
            Debug.Print "Normal: " & swMeasure.Normal
        End If
```

```
        If (Not (swMeasure.SpericalCenterDistance = -1)) Then
            Debug.Print "Spherical center distance: " & swMeasure.SpericalCenterDistance
        End If
```

```
        If (swMeasure.IsConcentricSpheres) Then
            Debug.Print "Are concentric spheres: " & swMeasure.IsConcentricSpheres
        End If
```

```
    Else
```

```
        Debug.Print "Invalid combination of selected entities."
```

```
    End If
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
