---
title: "Get Mates and Mate Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mates_and_Mate_Entities_Example_VBNET.htm"
---

# Get Mates and Mate Entities Example (VB.NET)

This example shows how to iterate through a FeatureManager design tree and get all of an assembly's mates and mate entities.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Iterates through the FeatureManager design tree to find
'    print Mates to the Immediate window.
' 3. Iterates through the subfeatures of Mates and prints each mate
'    entity's information to the Immediate window.
' 4. Examine the Immediate window.
'------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swFeat As Feature
        Dim swMateFeat As Feature = Nothing
        Dim swSubFeat As Feature
        Dim swMate As Mate2
        Dim swComp As Component2
        Dim swMateEnt(2) As MateEntity2
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim i As Integer
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\simple-block.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Get the first feature in the assembly
        swFeat = swModel.FirstFeature
        'Iterate over features in FeatureManager design tree
        Do While Not swFeat Is Nothing
            If "MateGroup" = swFeat.GetTypeName Then
                swMateFeat = swFeat
                Exit Do
            End If
            swFeat = swFeat.GetNextFeature
        Loop
        Debug.Print("  " & swMateFeat.Name)
        Debug.Print("")

        'Get first mate, which is a subfeature
        swSubFeat = swMateFeat.GetFirstSubFeature
        Do While Not swSubFeat Is Nothing
            swMate = swSubFeat.GetSpecificFeature2
            If Not swMate Is Nothing Then
                For i = 0 To 1
                    swMateEnt(i) = swMate.MateEntity(i)
                    Debug.Print("    " & swSubFeat.Name)
                    Debug.Print("      Type              = " & swMate.Type)
                    Debug.Print("      Alignment         = " & swMate.Alignment)
                    Debug.Print("      Can be flipped    = " & swMate.CanBeFlipped)
                    Debug.Print("")
                    swComp = swMateEnt(i).ReferenceComponent
                    Debug.Print("      Component         = " & swComp.Name2)
                    Debug.Print("      Mate entity type  = " & swMateEnt(i).ReferenceType)
                    Debug.Print("      (x,y,z)           = (" & swMateEnt(i).EntityParams(0) & ", " & swMateEnt(i).EntityParams(1) & ", " & swMateEnt(i).EntityParams(2) & ")")
                    Debug.Print("      (i,j,k)           = (" & swMateEnt(i).EntityParams(3) & ", " & swMateEnt(i).EntityParams(4) & ", " & swMateEnt(i).EntityParams(5) & ")")
                    Debug.Print("      Radius 1          = " & swMateEnt(i).EntityParams(6))
                    Debug.Print("      Radius 2          = " & swMateEnt(i).EntityParams(7))
                    Debug.Print("")
                Next i
                Debug.Print(" ")
            End If
            ' Get the next mate in MateGroup
            swSubFeat = swSubFeat.GetNextSubFeature
        Loop
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
