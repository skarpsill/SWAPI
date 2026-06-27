---
title: "Replace Component (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Replace_Component_Example_VBNET.htm"
---

# Replace Component (VB.NET)

This example shows how to replace a component with a different component.

```vb
 '---------------------------------------------------------------------------
  ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API Getting Started
 '    topic and ensure that the required DLLs are registered.
 ' 2. Copy and paste this code into a VB.NET console application
 '    in Microsoft Visual Studio.
 ' 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference to the project:
 '    a. Right-click the solution in Solution Explorer.
 '    b. Click Add Reference.
 '    c. Click Browse.
 '    d. Click:
 '       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 '    e. Click Add.
 '    f. Click Close.
 ' 4. Ensure that the model to open exists.
 ' 5. Substitute your_license_key with your SOLIDWORKS Document
 '    Manager license key.
 ' 6. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. The first instance of the shaft washer component is
 '    replaced with a lock washer in the document.
 '
 ' NOTE: The specified file should be backed up before running this macro,
 ' as it is used elsewhere. The macro uses a replacement that does not
 ' properly fit in the model.
 '--------------------------------------------------------------------------

  Imports System.Diagnostics
 Imports SolidWorks.Interop.swdocumentmgr

 Module Module1

     Sub Main()

         Dim swCf As SwDMClassFactory
         swCf = New SwDMClassFactory()
         Dim swDocMgr As SwDMApplication
         swDocMgr = DirectCast(swCf.GetApplication("your_license_key"), SwDMApplication)
         Dim swDoc12 As SwDMDocument12
         Dim res As SwDmDocumentOpenError
         Dim dt As SwDmDocumentType
         dt = SwDmDocumentType.swDmDocumentAssembly
         Dim filename As String

         filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\98food processor.sldasm"
         swDoc12 =  TryCast(swDocMgr.GetDocument(filename, dt, False, res), SwDMDocument12)

         If swDoc12 Is Nothing Or (res <> SwDmDocumentOpenError.swDmDocumentOpenErrorNone)  Then
             Debug.Print("Error opening file...")
             Return
         End If

         Debug.Print("Getting the active configuration...")
         Dim activeConfig As SwDMConfiguration8
         Dim configMgr As SwDMConfigurationMgr
         configMgr = swDoc12.ConfigurationManager
         configMgr.GetConfigurationNames()
         activeConfig = TryCast(configMgr.GetConfigurationByName(configMgr.GetActiveConfigurationName()), SwDMConfiguration8)
         If activeConfig Is Nothing Then
             Debug.Print("Error getting the active configuration...")
             Return
         End If

         Debug.Print("Getting the components of the active configuration...")
         Dim vComponents As Object()
         vComponents = DirectCast(activeConfig.GetComponents(), Object())
         Dim swDmComponent As SwDMComponent6

         Dim i As  Integer
         For i = 0 To vComponents.Length - 1
             swDmComponent = DirectCast(vComponents(i), SwDMComponent6)
             If swDmComponent.Name = "shaft washer" Then
                 Dim bResult As Boolean = swDmComponent.Replace("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\lockwasher.sldprt", "Default", False)
                 Debug.Print("Replacing shaft washer with lock washer...")
                 Debug.Print(bResult.ToString())
                 Exit For
             End If
         Next

         swDoc12.Save()
         swDoc12.CloseDoc()

     End Sub

 End Module
```
