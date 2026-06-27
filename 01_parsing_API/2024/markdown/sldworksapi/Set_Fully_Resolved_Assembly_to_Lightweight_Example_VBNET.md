---
title: "Set Fully Resolved Assembly to Lightweight Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Fully_Resolved_Assembly_to_Lightweight_Example_VBNET.htm"
---

# Set Fully Resolved Assembly to Lightweight Example (VB.NET)

This example shows how to set a fully resolved assembly to lightweight.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Open a fully resolved assembly document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Sets all assembly components to lightweight.
' 2. Examine the Immediate window and FeatureManager design tree.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssy As AssemblyDoc
        Dim swConfig As Configuration
        Dim swConfigMgr As ConfigurationManager
        Dim swRootComp As Component2
        Dim bRet As Boolean

        swModel = swApp.ActiveDoc
        swAssy = swModel
        swConfigMgr = swModel.ConfigurationManager
        swConfig = swConfigMgr.ActiveConfiguration
        swRootComp = swConfig.GetRootComponent3(True)
        Debug.Print("File = " & swModel.GetPathName)
        SetComponentLightWeight("  ", swRootComp)

        ' Update in-context features
        bRet = swModel.ForceRebuild3(False) : Debug.Assert(bRet)

    End Sub

    Sub SetComponentLightWeight(ByVal sPadStr As String, ByVal swComp As Component2)
        Dim vChildArr As Object
        Dim swChildComp As Component2
        Dim swChildModel As ModelDoc2
        Dim nRetVal As Integer
        Dim nDocType As Integer
        Dim i As Integer

        Debug.Print(sPadStr & swComp.Name2 & " [" & CBool(swComp.Visible) & "]")
        vChildArr = swComp.GetChildren
        For i = 0 To UBound(vChildArr)
            swChildComp = vChildArr(i)
            ' Is Nothing if another instance has been previously set to lightweight
            swChildModel = swChildComp.GetModelDoc2
            If Not swChildModel Is Nothing Then
                nDocType = swChildModel.GetType
            Else
                nDocType = swDocumentTypes_e.swDocNONE
            End If
            nRetVal = swChildComp.SetSuppression2(swComponentSuppressionState_e.swComponentLightweight)
            If swDocumentTypes_e.swDocPART = nDocType Or swDocumentTypes_e.swDocNONE = nDocType Then
                Debug.Assert(swComponentResolveStatus_e.swResolveNotPerformed = nRetVal)
            Else
                ' Cannot set a sub-assembly to lightweight; must set each part to lightweight
                Debug.Assert(swDocumentTypes_e.swDocASSEMBLY = swChildModel.GetType)
                Debug.Assert(swComponentResolveStatus_e.swResolveError = nRetVal)
            End If
            ' Recurse into this component
            SetComponentLightWeight(sPadStr & "  ", swChildComp)

        Next i
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
