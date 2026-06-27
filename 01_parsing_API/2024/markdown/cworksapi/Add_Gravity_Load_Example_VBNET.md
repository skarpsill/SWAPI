---
title: "Add Gravity Load Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Gravity_Load_Example_VBNET.htm"
---

# Add Gravity Load Example (VB.NET)

This example shows how to add a gravity load to a static study.

```vb
  '------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim Part As ModelDoc2
         Dim fileName As String
         Dim errors As Integer
         Dim warnings As Integer
         Dim errCode As Integer
         Dim longstatus As Integer
         Dim COSMOSWORKS As CosmosWorks
         Dim CWAddinCallBack As CWAddincallBack
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim mesh As CWMesh
         Dim StaticOptions As CWStaticStudyOptions
         Dim lrMgr As CWLoadsAndRestraintsManager
         Dim Gravity As CWGravity
         Dim dispEntity As Object
         Dim str1 As String
         Dim var1 As Object = Nothing
         Dim xval As Double, yval As Double, zval As Double

         Const MeshEleSize As Double = 1.4769
         Const MeshTol As Double = 0.073847

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\tjoint.sldprt"
         Part = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, 1, "", errors, warnings)

         CWAddinCallBack = SwApp.GetAddInObject("SldWorks.Simulation")
         COSMOSWORKS = CWAddinCallBack.COSMOSWORKS

         ActDoc = COSMOSWORKS.ActiveDoc()

         StudyMngr = ActDoc.StudyManager()
         StudyMngr.ActiveStudy = 1
         Study = StudyMngr.GetStudy(StudyMngr.ActiveStudy)

         'Select top plane for gravity's direction reference
         str1 = "64,31,0,0,1,0,0,0,255,254,255,0,0,0,0,0,3,0,0,0"
         StringtoArray(str1, var1)
         dispEntity = Part.Extension.GetObjectByPersistReference3((var1), longstatus)

         lrMgr = Study.LoadsAndRestraintsManager

         'Delete pressure loads
         lrMgr.DeleteLoadsAndRestraints("Pressure-1")
         lrMgr.DeleteLoadsAndRestraints("Pressure-2")

         'Add gravity load
         Gravity = lrMgr.AddGravity(dispEntity, errCode)

         Gravity.GetGravitationalAcclerationValues(xval, yval, zval)
         Debug.Print("Gravity acceleration:")
         Debug.Print("  Direction 1: " & xval)
         Debug.Print("     Reverse? (True=yes, False=no) " & Gravity.ReverseDirectionAlongPlaneDir1_2)
         Debug.Print("  Direction 2: " & yval)
         Debug.Print("     Reverse? (True=yes, False=no) " & Gravity.ReverseDirectionAlongPlaneDir2_2)
         Debug.Print("  Normal direction: " & zval)
         Debug.Print("     Reverse? (True=yes, False=no) " & Gravity.ReverseDirectionNormalToPlane2)
         Debug.Print("  Units as defined in swsUnitSystem_e: " & Gravity.Unit)

         'Mesh
         mesh = Study.Mesh
         mesh.MesherType = 0
         mesh.Quality = 0
         errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)

         StaticOptions = Study.StaticStudyOptions
         StaticOptions.SolverType = 2

         'Run analysis
         errCode = Study.RunAnalysis

     End Sub

     Sub StringtoArray(ByVal inputSTR As String, ByRef varEntity As Object)

         Dim PID() As Byte
         Dim i As Integer

         varEntity = Split(inputSTR, ",")

         ReDim PID(UBound(varEntity))

         For i = 0 To (UBound(varEntity) - 1)
             PID(i) = varEntity(i)
         Next i

         varEntity = PID

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
