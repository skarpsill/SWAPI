---
title: "Get Sketch Slot Data (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Slot_Data_Example_vb.htm"
---

# Get Sketch Slot Data (VBA)

This example shows how to get sketch slot data.

```vb
'-------------------------------------
' Preconditions: Model document is active and contains
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}a Sketch3 feature with one or more
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}sketch slots.
'
' Postconditions: None
'--------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim longstatus As Long, longwarnings As Long
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketch As SldWorks.Sketch
Dim iSlotCount As Integer
Dim vSketchSlots As Variant
Dim vSketchSlot As Variant
Dim swSketchSlot As SldWorks.SketchSlot
Dim i As Integer
Dim swFeature As SldWorks.Feature
Dim swMathPoint As SldWorks.MathPoint
Dim vArray As Variant
Dim swSketchPoint As SldWorks.SketchPoint
Dim vSketchPtID As Variant

Sub main()

Set swApp = Application.SldWorks

Set swPart = swApp.OpenDoc6("C:\test\Slots.SLDPRT", 1, 0, "", longstatus, longwarnings)
Set swSketchMgr = swPart.SketchManager

Set swFeature = swPart.FeatureByName("Sketch3")
Set swSketch = swFeature.GetSpecificFeature2()
iSlotCount = swSketch.GetSketchSlotCount
Debug.Print "Number of slots: " & iSlotCount
Debug.Print " "
vSketchSlots = swSketch.GetSketchSlots

For Each vSketchSlot In vSketchSlots
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSketchSlot = vSketchSlot
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Length: " & swSketchSlot.Length
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Width: " & swSketchSlot.Width
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "LengthType: " & swSketchSlot.LengthType
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swMathPoint = swSketchSlot.GetCenterPoint
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vArray = swMathPoint.ArrayData
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "CenterPoint (x,y,z): " & vArray(0) & "," & vArray(1) & "," & vArray(2)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSketchPoint = swSketchSlot.GetCenterPointHandle
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "CenterPointHandle ISketchPoint(x,y,z): " & swSketchPoint.X & "," & swSketchPoint.Y & "," & swSketchPoint.Z & vbCrLf
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vSketchPtID = swSketchPoint.GetID
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}IDPt(" & i & ") = [" & vSketchPtID(0) & ", " & vSketchPtID(1) & "]" & vbCrLf
Next

End Sub
```
