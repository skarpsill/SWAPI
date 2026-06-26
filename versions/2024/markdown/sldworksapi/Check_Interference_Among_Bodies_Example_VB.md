---
title: "Check Interference Among Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Interference_Among_Bodies_Example_VB.htm"
---

# Check Interference Among Bodies Example (VBA)

This example shows how to check interference among bodies in a part document.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Finds a body in a solid body folder that interferes with
'    one or more solid bodies in another solid body folder.
' 2. Examine the Immediate window and expand Cut list(31) >
'    Sub-weldment(8).
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim swPartDoc As SldWorks.ModelDoc2
Dim swFeature As SldWorks.Feature
Dim swBodyFolder As SldWorks.BodyFolder
Dim BodyFolder As SldWorks.BodyFolder
Dim toolBodyList As Variant
Dim targetBodyList As Variant
Dim contLoop As Boolean
Dim areBodyClash As Boolean
Dim swModeler As SldWorks.Modeler
Dim vBodies As Variant
Dim vFaces1 As Variant
Dim vFaces2 As Variant
Dim sldBody1 As SldWorks.Body2
Dim sldBody2 As SldWorks.Body2
Dim sizeOfOut1, sizeOfOut2, sizeOfOut3 As Long
```

```
Sub GetVariantOfBody(swFeature As SldWorks.Feature, bodyList As Variant)
    Dim tt As Variant
    Dim FeatType As String
    Dim FeatTypeName As String
```

```
    FeatType = swFeature.Name
    FeatTypeName = swFeature.GetTypeName2
    Debug.Print FeatType & " [" & FeatTypeName & "]"
```

```
    Set swBodyFolder = swFeature.GetSpecificFeature2
    Dim count As Long
    count = swBodyFolder.GetBodyCount
    If (count < 1) Then
        MsgBox ("There are no bodies. Create a body in the folder.")
    Else
        bodyList = swBodyFolder.GetBodies
    End If
End Sub
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swPartDoc = swApp.ActiveDoc
    Set swFeature = swPartDoc.FirstFeature
    Set swModeler = swApp.GetModeler
```

```
    contLoop = True
```

```
    While Not swFeature Is Nothing And contLoop = True
        Dim Name As String
        Name = swFeature.GetTypeName2
        If (Name = "SolidBodyFolder") Then
            contLoop = False
```

```
            GetVariantOfBody swFeature, targetBodyList
```

```
            Set swFeature = swFeature.GetFirstSubFeature
```

```
            GetVariantOfBody swFeature, toolBodyList
```

```
            Dim i As Long
```

```
            areBodyClash = swModeler.CheckInterference3(targetBodyList, toolBodyList, (swBodyInterference_ReturnInterferingObject + swBodyInterference_IncludeCoincidentFaces), vFaces1, vFaces2, vBodies)
            If (areBodyClash) Then
                sizeOfOut1 = UBound(vFaces1)
                sizeOfOut2 = UBound(vFaces2)
                sizeOfOut3 = UBound(vBodies)
                Debug.Print ("  Returning interfering body (faces touching each other):")
                Debug.Print ("    No. of faces that interfered from the first body with the second body")
                Debug.Print ("      " & sizeOfOut1 + 1)
                Debug.Print ("    No. of faces that interfered from the second body with the first body:")
                Debug.Print ("      " & sizeOfOut2 + 1)
                Debug.Print ("    No. of interfering bodies")
                Debug.Print ("      " & sizeOfOut3 + 1)
            End If
```

```
            Debug.Print " "
```

```
            areBodyClash = swModeler.CheckInterference3(targetBodyList, toolBodyList, (swBodyInterference_OptionDefault), vFaces1, vFaces2, vBodies)
            If (areBodyClash) Then
                sizeOfOut1 = UBound(vFaces1)
                sizeOfOut2 = UBound(vFaces2)
                sizeOfOut3 = UBound(vBodies)
                Debug.Print ("  Returning interfering body (faces not touching each other): ")
                Debug.Print ("    No. of faces1")
                Debug.Print ("    " & sizeOfOut1 + 1)
                Debug.Print ("    No. of faces2")
                Debug.Print ("    " & sizeOfOut2 + 1)
                Debug.Print ("    No. of bodies")
                Debug.Print ("    " & sizeOfOut3 + 1)
            End If
        Else
            Set swFeature = swFeature.GetNextFeature
        End If
    Wend
```

```
End Sub
```
