---
title: "Custom Colorize a Model Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Custom_Colorize_a_Model_Example_VBNET.htm"
---

# Custom Colorize a Model Example (VB.NET)

This example shows how to colorize a model.

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET add-in project in Microsoft Visual Studio.
' 2. Copy this sample code to SwAddin.vb of the new project.
' 3. Ensure that PMPHandler.vb is implementing a compatible interface.
' 4. Compile and run the project.
' 5. In SOLIDWORKS open public_documents\samples\tutorial\api\wrench.sldasm.
' 6. Select View > Display > Curvature.
'
' Postconditions:
' 1. The model is colorized as a function of
'    Value1 = (double)(vertexCoordX + vertexCoordY + vertexCoordZ);
' 2. Value1 is displayed and refreshed as the cursor moves over the model.
'
' NOTE: Because the model is used elsewhere,
' do not save changes when closing it.
'----------------------------------------------------------------------------
```

```vb
Imports System
 Imports System.Collections
 Imports System.Reflection
 Imports System.Runtime.InteropServices

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports SOLIDWORKSTools
 Imports SOLIDWORKSTools.File

 Imports System.Collections.Generic
 Imports System.Diagnostics

 <Guid("3d612c15-6c1c-4d5e-b0f3-09e4c9cc8dc7")> _
     <ComVisible(True)> _
     <SwAddin( _
         Description:="SwVBAddin1 description", _
         Title:="SwVBAddin1", _
         LoadAtStartup:=True _
         )> _
         Public Class SwAddin
     Implements SolidWorks.Interop.swpublished.SwAddin

 #Region "Local Variables"
     Dim WithEvents iSwApp As SldWorks
     Dim iCmdMgr As ICommandManager
     Dim addinID As Integer
     Dim openDocs As Hashtable
     Dim colorDocs As Hashtable
     Dim SwEventPtr As SldWorks
     Dim ppage As UserPMPage
     Dim iBmp As BitmapHandler

     ' Public Properties
     ReadOnly Property SwApp() As SldWorks
         Get
             Return iSwApp
         End Get
     End Property

     ReadOnly Property CmdMgr() As ICommandManager
         Get
             Return iCmdMgr
         End Get
     End Property

     ReadOnly Property OpenDocumentsTable() As Hashtable
         Get
             Return openDocs
         End Get
     End Property
 #End  Region

 #Region "SOLIDWORKS Registration"

     <ComRegisterFunction()> Public Shared Sub RegisterFunction(ByVal t As  Type)

         ' Get Custom Attribute: SwAddinAttribute
         Dim attributes() As Object
         Dim SWattr As SwAddinAttribute = Nothing

         attributes = System.Attribute.GetCustomAttributes(GetType(SwAddin), GetType(SwAddinAttribute))

         If attributes.Length > 0 Then
             SWattr = DirectCast(attributes(0), SwAddinAttribute)
         End If
         Try
             Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
             Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

             Dim keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString() + "}"
             Dim addinkey As Microsoft.Win32.RegistryKey = hklm.CreateSubKey(keyname)
             addinkey.SetValue(Nothing, 0)
             addinkey.SetValue("Description", SWattr.Description)
             addinkey.SetValue("Title", SWattr.Title)

             keyname = "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString() + "}"
             addinkey = hkcu.CreateSubKey(keyname)
             addinkey.SetValue(Nothing, SWattr.LoadAtStartup, Microsoft.Win32.RegistryValueKind.DWord)
         Catch nl As System.NullReferenceException
             Console.WriteLine("There was a problem registering this dll: SWattr is null.\n " & nl.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: SWattr is null.\n" & nl.Message)
         Catch e As System.Exception
             Console.WriteLine("There was a problem registering this dll: " & e.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: " & e.Message)
         End Try
     End Sub

     <ComUnregisterFunction()> Public Shared Sub UnregisterFunction(ByVal t As  Type)
         Try
             Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
             Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

             Dim keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString() + "}"
             hklm.DeleteSubKey(keyname)

             keyname = "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString() + "}"
             hkcu.DeleteSubKey(keyname)
         Catch nl As System.NullReferenceException
             Console.WriteLine("There was a problem unregistering this dll: SWattr is null.\n " & nl.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: SWattr is null.\n" & nl.Message)
         Catch e As System.Exception
             Console.WriteLine("There was a problem unregistering this dll: " & e.Message)
             System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: " & e.Message)
         End Try

     End Sub

 #End  Region

 #Region "ISwAddin Implementation"

     Function ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Integer) As  Boolean  Implements SolidWorks.Interop.swpublished.SwAddin.ConnectToSW
         iSwApp = ThisSW
         addinID = Cookie

         ' Setup callbacks
         iSwApp.SetAddinCallbackInfo(0, Me, addinID)

         'Setup the Event Handlers
         SwEventPtr = iSwApp
         openDocs = New Hashtable
         colorDocs = New Hashtable
         AttachEventHandlers()

         ConnectToSW = True
     End Function

     Function DisconnectFromSW() As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.DisconnectFromSW

         DetachEventHandlers()

         System.Runtime.InteropServices.Marshal.ReleaseComObject(iCmdMgr)
         iCmdMgr = Nothing
         System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp)
         iSwApp = Nothing
         'The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
         GC.Collect()
         GC.WaitForPendingFinalizers()

         GC.Collect()
         GC.WaitForPendingFinalizers()

         DisconnectFromSW = True
     End Function
 #End  Region

 #Region "Event Methods"
     Sub AttachEventHandlers()
         AttachSWEvents()

         'Listen for events on all currently open docs
         AttachEventsToAllDocuments()
     End Sub

     Sub DetachEventHandlers()
         DetachSWEvents()

         'Close events on all currently open docs
         Dim docHandler As DocumentEventHandler
         Dim key As ModelDoc2
         Dim numKeys As Integer
         numKeys = openDocs.Count
         If numKeys > 0 Then
             Dim keys() As Object = New  Object(numKeys - 1) {}

             'Remove all document event handlers
             openDocs.Keys.CopyTo(keys, 0)
             For Each key In keys
                 docHandler = openDocs.Item(key)
                 docHandler.DetachEventHandlers()  'This also removes the pair from the hash
                 docHandler = Nothing
                 key = Nothing
             Next
         End If
     End Sub

     Sub AttachSWEvents()
         Try
             AddHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
             AddHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
             AddHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
             AddHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
             AddHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
         Catch e As  Exception
             Console.WriteLine(e.Message)
         End Try
     End Sub

     Sub DetachSWEvents()
         Try
             RemoveHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
             RemoveHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
             RemoveHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
             RemoveHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
             RemoveHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
         Catch e As  Exception
             Console.WriteLine(e.Message)
         End Try
     End Sub

     Sub AttachEventsToAllDocuments()
         Dim modDoc As ModelDoc2
         modDoc = iSwApp.GetFirstDocument()
         While Not modDoc Is  Nothing
             If Not openDocs.Contains(modDoc) Then
                 AttachModelDocEventHandler(modDoc)
             End If
             modDoc = modDoc.GetNext()
         End While
     End Sub

     Function AttachModelDocEventHandler(ByVal modDoc As ModelDoc2) As  Boolean
         If modDoc Is Nothing Then
             Return False
         End If
         Dim docHandler As DocumentEventHandler = Nothing

         If Not openDocs.Contains(modDoc) Then
             Dim modExt As ModelDocExtension = modDoc.Extension

             Dim colorInt As New  ColorContour()
             modExt.InstallModelColorizer(colorInt)
             colorDocs.Add(modDoc, colorInt)

             Select Case modDoc.GetType
                 Case swDocumentTypes_e.swDocPART
                     docHandler = New PartEventHandler()
                 Case swDocumentTypes_e.swDocASSEMBLY
                     docHandler = New AssemblyEventHandler()
                 Case swDocumentTypes_e.swDocDRAWING
                     docHandler = New DrawingEventHandler()
             End Select

             docHandler.Init(iSwApp, Me, modDoc)
             docHandler.AttachEventHandlers()
             openDocs.Add(modDoc, docHandler)
         End If
     End Function

     Sub DetachModelEventHandler(ByVal modDoc As ModelDoc2)
         Dim docHandler As DocumentEventHandler
         docHandler = openDocs.Item(modDoc)
         openDocs.Remove(modDoc)
         modDoc = Nothing
         docHandler = Nothing
     End Sub
 #End  Region

 #Region "Event Handlers"
     Function SldWorks_ActiveDocChangeNotify() As Integer
         'TODO: Add your implementation here
     End Function

     Function SldWorks_DocumentLoadNotify2(ByVal docTitle As String, ByVal docPath As String) As  Integer

     End Function

     Function SldWorks_FileNewNotify2(ByVal newDoc As Object, ByVal doctype As Integer, ByVal templateName As String) As  Integer
         AttachEventsToAllDocuments()
     End Function

     Function SldWorks_ActiveModelDocChangeNotify() As Integer
         'TODO: Add your implementation here
     End Function

     Function SldWorks_FileOpenPostNotify(ByVal FileName As String) As  Integer
         AttachEventsToAllDocuments()
     End Function
 #End  Region

 End  Class
 Public Class ColorContour
     Implements ISwColorContour1

 #Region "ISwColorContour Members"

     Public Function  Color(ByVal Value1 As Double) As  Integer  Implements SolidWorks.Interop.swpublished.ISwColorContour1.Color
         ' Assign colors to Value ranges
         If (Value1 > 0.0) And (Value1 <= 0.025) Then
             Return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Coral)
         ElseIf (Value1 > 0.025) And (Value1 <= 0.05) Then
             Return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Salmon)
         ElseIf Value1 > 0.05 Then
             Return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Pink)
         Else
             Return System.Drawing.ColorTranslator.ToWin32(System.Drawing.Color.Red)
         End If

     End Function

     Public Function  DisplayString(ByVal Value1 As Double) As  String  Implements SolidWorks.Interop.swpublished.ISwColorContour1.DisplayString
         ' Return what is displayed in the view for the given Value
         Return "Value is: " + Value1.ToString()
     End Function

     Public Function  NeedsUpdate() As Boolean Implements SolidWorks.Interop.swpublished.ISwColorContour1.NeedsUpdate
         ' Return whether SOLIDWORKS needs to refresh the view
         Return True
     End Function

     Public Function  Value(ByVal face As Object, ByVal vertexCoordX As Single, ByVal vertexCoordY As Single, ByVal vertexCoordZ As Single, ByVal normalCoordsX As Single, ByVal normalCoordsY As Single, _
     ByVal normalCoordsZ As Single, ByRef Value1 As Double) As  Integer  Implements SolidWorks.Interop.swpublished.ISwColorContour1.Value
         ' Define a Value for the selected coordinates
         Value1 = CDbl(vertexCoordX + vertexCoordY + vertexCoordZ)

         Return 0

     End Function

 #End  Region
 End  Class
```
