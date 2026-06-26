---
title: "Add Gravity Load Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Gravity_Load_Example_VB.htm"
---

# Add Gravity Load Example (VBA)

This example shows how to add a gravity load to a static study.

```vb
 '------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Verify that the specified model document exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the document.
 ' 2. Activates Ready - 8 plies.
 ' 3. Deletes two pressure loads from Ready - 8 plies.
 ' 4. Adds the Gravity-1 load to Ready - 8 plies.
 ' 5. Prints the Gravity-1 properties to the Immediate window.
 ' 6. Meshes the part.
 ' 7. Sets the solver type.
 ' 8. Analyzes Ready - 8 plies.
 ' 9. Inspect the Immediate window, the Simulation study tree,
 '    and the graphics area.
 '
 ' NOTE: Because this part document is used elsewhere, do not save any changes.
 '-----------------------------------------------------------------------------
 Option Explicit
Sub main()
     Dim SwApp           As SldWorks.SldWorks
     Dim Part            As SldWorks.ModelDoc2
     Dim fileName        As String
     Dim errors          As Long
     Dim warnings        As Long
     Dim errCode         As Long
     Dim longstatus      As Long
     Dim COSMOSWORKS     As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc          As CosmosWorksLib.CWModelDoc
     Dim StudyMngr       As CosmosWorksLib.CWStudyManager
     Dim Study           As CosmosWorksLib.CWStudy
     Dim mesh            As CosmosWorksLib.CWMesh
     Dim StaticOptions   As CosmosWorksLib.CWStaticStudyOptions
     Dim lrMgr           As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim Gravity         As CosmosWorksLib.CWGravity
     Dim dispEntity      As Object
     Dim str1            As String
     Dim var1            As Variant
     Dim xval As Double, yval As Double, zval As Double

    Const MeshEleSize   As Double = 1.4769
     Const MeshTol       As Double = 0.073847

    Set SwApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tjoint.sldprt"
     Set Part = SwApp.OpenDoc6(fileName, swDocPART, 1, "", errors, warnings)
    Set CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
    Set ActDoc = COSMOSWORKS.ActiveDoc()
    Set StudyMngr = ActDoc.StudyManager()
     StudyMngr.ActiveStudy = 1
     Set Study = StudyMngr.GetStudy(StudyMngr.ActiveStudy)

    'Select top plane for gravity's direction reference
     str1 = "64,31,0,0,1,0,0,0,255,254,255,0,0,0,0,0,3,0,0,0"
     StringtoArray str1, var1
     Set dispEntity = Part.Extension.GetObjectByPersistReference3((var1), longstatus)

    Set lrMgr = Study.LoadsAndRestraintsManager

    'Delete pressure loads
     lrMgr.DeleteLoadsAndRestraints ("Pressure-1")
     lrMgr.DeleteLoadsAndRestraints ("Pressure-2")

    'Add gravity load
     Set Gravity = lrMgr.AddGravity(dispEntity, errCode)

     Gravity.GetGravitationalAcclerationValues xval, yval, zval
     Debug.Print "Gravity acceleration:"
     Debug.Print "  Direction 1: " & xval
     Debug.Print "     Reverse? (True=yes, False=no) " & Gravity.ReverseDirectionAlongPlaneDir1_2
     Debug.Print "  Direction 2: " & yval
     Debug.Print "     Reverse? (True=yes, False=no) " & Gravity.ReverseDirectionAlongPlaneDir2_2
     Debug.Print "  Normal direction: " & zval
     Debug.Print "     Reverse? (True=yes, False=no) " & Gravity.ReverseDirectionNormalToPlane2
     Debug.Print "  Units as defined in swsUnitSystem_e: " & Gravity.Unit

    'Mesh
     Set mesh = Study.Mesh
     mesh.MesherType = 0
     mesh.Quality = 0
     errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)

    Set StaticOptions = Study.StaticStudyOptions
     StaticOptions.SolverType = 2

    'Run analysis
     errCode = Study.RunAnalysis

 End Sub
Sub StringtoArray(inputSTR As String, varEntity As Variant)
   Dim PID() As Byte
    Dim i As Integer
   varEntity = Split(inputSTR, ",")
   ReDim PID(UBound(varEntity))
   For i = 0 To (UBound(varEntity) - 1)
       PID(i) = varEntity(i)
    Next i
   varEntity = PID
End Sub
```
