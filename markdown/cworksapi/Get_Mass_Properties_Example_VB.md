---
title: "Get Mass Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Mass_Properties_Example_VB.htm"
---

# Get Mass Properties Example (VBA)

This example shows how to get the mass properties of a study.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation  version type library).
 ' 3. Ensure that the specified file exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions: Prints some mass properties of the Ready study to the
 ' Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swAddin As CosmosWorksLib.CwAddincallback
 Dim ssApp As CosmosWorksLib.CosmosWorks
 Dim ssModelDoc As CosmosWorksLib.CWModelDoc
 Dim ssStudyMgr As CosmosWorksLib.CWStudyManager
 Dim ssStudy As CosmosWorksLib.CWStudy
 Dim massPropMgr As CosmosWorksLib.CWMassPropertiesManager
 Dim docName As String
 Dim errors As Long
 Dim warnings As Long
 Dim studyName As String
 Dim studyType As Long
 Dim comObj As Variant
 Dim moiObj As Variant
 Dim moiocsObj As Variant
 Dim paiObj As Variant
 Dim pmiObj As Variant
 Dim varArray As Variant
 Dim var1 As Variant, var2 As Variant
 Dim pDisp1 As Object, pDisp2 As Object
 Dim selection1 As String
 Dim selection2 As String

Sub main()
    Set swApp = Application.SldWorks
     docName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Contact\quartereyebar.sldasm"
     swApp.OpenDoc6 docName, swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings

    Set Part = swApp.ActiveDoc

    Set swAddin = swApp.GetAddInObject("SldWorks.Simulation")
     Set ssApp = swAddin.CosmosWorks
     Set ssModelDoc = ssApp.ActiveDoc
     Set ssStudyMgr = ssModelDoc.StudyManager

    Set ssStudy = ssStudyMgr.GetStudy(0)
     studyName = ssStudy.Name
     Debug.Print "Study name: " & studyName
     studyType = ssStudy.AnalysisType
     Debug.Print "  Type as defined in swsAnalysisStudyType_e: " & studyType

    Set massPropMgr = ssStudy.GetMassPropertiesManager
    selection1 = "245,35,0,0,4,0,0,0,255,254,255,27,113,0,117,0,97,0,114,0,116,0,101,0,114,0,98,0,111,0,108,0,116,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,1,0,0,0,101,0,0,0"
     selection1 = selection1 & ",Type=3"
     StringtoArray selection1, var1
     Set pDisp1 = Part.Extension.GetObjectByPersistReference3((var1), errors)
    selection2 = "245,35,0,0,4,0,0,0,255,254,255,29,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,3,0,0,0,103,0,0,0,102,0,0,0,101,0,0,0"
     selection2 = selection2 & ",Type=3"
     StringtoArray selection2, var2
     Set pDisp2 = Part.Extension.GetObjectByPersistReference3((var2), errors)
    varArray = Array(pDisp1, pDisp2)

    massPropMgr.SetCoordinateSystemToDefault
    errors = massPropMgr.AddBodies(varArray)
     comObj = massPropMgr.GetCenterOfMass
     moiObj = massPropMgr.GetMomentOfInertia
     moiocsObj = massPropMgr.GetMomentOfInertiaAtOutputCoordinateSystem
     paiObj = massPropMgr.GetPrincipalAxesOfInertia
     pmiObj = massPropMgr.GetPrincipalMomentOfInertia
     Debug.Print "  Mass properties:"
     Debug.Print "    Surface area (square meters): " & massPropMgr.Area
     Debug.Print "    Mass (kilograms): " & massPropMgr.Mass
     Debug.Print "    Volume (cubic meters): " & massPropMgr.Volume
     Debug.Print "    Center of mass: "
     Debug.Print "        x: " & comObj(0)
     Debug.Print "        y: " & comObj(1)
     Debug.Print "        z: " & comObj(2)
     Debug.Print "    Moment of inertia (kilograms * meters squared): "
     Debug.Print "        lxx: " & moiObj(0)
     Debug.Print "        lxy: " & moiObj(1)
     Debug.Print "        lxz: " & moiObj(2)
     Debug.Print "        lyx: " & moiObj(3)
     Debug.Print "        lyy: " & moiObj(4)
     Debug.Print "        lyz: " & moiObj(5)
     Debug.Print "        lzx: " & moiObj(6)
     Debug.Print "        lzy: " & moiObj(7)
     Debug.Print "        lzz: " & moiObj(8)
     Debug.Print "    Moment of inertia with respect to output coordinate system (kilograms * square meters): "
     Debug.Print "        lxx: " & moiocsObj(0)
     Debug.Print "        lxy: " & moiocsObj(1)
     Debug.Print "        lxz: " & moiocsObj(2)
     Debug.Print "        lyx: " & moiocsObj(3)
     Debug.Print "        lyy: " & moiocsObj(4)
     Debug.Print "        lyz: " & moiocsObj(5)
     Debug.Print "        lzx: " & moiocsObj(6)
     Debug.Print "        lzy: " & moiocsObj(7)
     Debug.Print "        lzz: " & moiocsObj(8)
     Debug.Print "    Coefficients of the principal axes of inertia with respect to center of mass: "
     Debug.Print "        Axis1_x: " & paiObj(0)
     Debug.Print "        Axis1_y: " & paiObj(1)
     Debug.Print "        Axis1_z: " & paiObj(2)
     Debug.Print "        Axis2_x: " & paiObj(3)
     Debug.Print "        Axis2_y: " & paiObj(4)
     Debug.Print "        Axis2_z: " & paiObj(5)
     Debug.Print "        Axis3_x: " & paiObj(6)
     Debug.Print "        Axis3_y: " & paiObj(7)
     Debug.Print "        Axis3_z: " & paiObj(8)
     Debug.Print "    Principal moments of inertia with respect to center of mass: "
     Debug.Print "        Px: " & pmiObj(0)
     Debug.Print "        Py: " & pmiObj(1)
     Debug.Print "        Pz: " & pmiObj(2)

 End Sub
Function StringtoArray(inputSTR As String, varEntity As Variant)
    Dim PID() As Byte
    Dim i As Integer
    varEntity = Split(inputSTR, ",")
    ReDim PID(UBound(varEntity))
    For i = 0 To (UBound(varEntity) - 1)
     PID(i) = varEntity(i)
    Next i
    varEntity = PID
 End Function
```
