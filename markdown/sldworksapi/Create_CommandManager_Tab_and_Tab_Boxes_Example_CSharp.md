---
title: "Create CommandManager Tab and Tab Boxes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_CommandManager_Tab_and_Tab_Boxes_Example_CSharp.htm"
---

# Create CommandManager Tab and Tab Boxes Example (C#)

This example shows how to create an add-in that creates a CommandManager
tab and tab boxes.

NOTES:

- This sample code is part of a project that was
  built using the C# Add-In Wizard.
- To run this sample code, you need to create a complete
  C# project.
- Your add-in must check to see if the tab already
  exists. If the tab already exists, then you should use that tab instead
  of creating a new tab. If your add-in does not check for an existing tab,
  then SOLIDWORKS will create a new tab each time it starts up.
- Users can add buttons to and remove buttons from
  your CommandManager tab. However, if your add-in removes the CommandManager
  tab upon exiting SOLIDWORKS, then any user customizations will be lost.

\\------------------------------------------------------------------------------------------------------------------------------

#### \\ SwAddin.cs

```vb
using System;
using System.Diagnostics;
using System.Collections;
using System.Reflection;
using System.Runtime.InteropServices;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swpublished;
using SolidWorksTools;
using SolidWorksTools.File;
namespace SwCSharpAddin1
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}[Guid("c5ede50f-7484-416b-9425-ca49f565e48e")]
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}[ComVisible(true)]
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}[SwAddin(Description = "test description", Title = "test", LoadAtStartup = true)]
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public class SwAddin : SolidWorks.Interop.swpublished.SwAddin
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region "Local Variables"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SldWorks iSwApp;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ICommandManager iCmdMgr;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int addinID;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Hashtable openDocs;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SldWorks SwEventPtr;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}UserPMPage ppage;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Public Properties
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks SwApp
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}get { return iSwApp; }
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public ICommandManager CmdMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}get { return iCmdMgr; }
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public Hashtable OpenDocumentsTable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}get { return openDocs; }
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region "SOLIDWORKS Registration"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}[ComRegisterFunction()]
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public static void RegisterFunction(Type t)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get Custom Attribute: SwAddinAttribute
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] attributes = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwAddinAttribute SWattr = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}attributes = System.Attribute.GetCustomAttributes(typeof(SwAddin), typeof(SwAddinAttribute));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (attributes.Length > 0)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SWattr = (SwAddinAttribute)attributes[0];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}addinkey.SetValue(null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}addinkey.SetValue("Description", SWattr.Description);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}addinkey.SetValue("Title", SWattr.Title);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}addinkey = hkcu.CreateSubKey(keyname);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}addinkey.SetValue(null, SWattr.LoadAtStartup, Microsoft.Win32.RegistryValueKind.DWord);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}[ComUnregisterFunction()]
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public static void UnregisterFunction(Type t)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}hklm.DeleteSubKey(keyname);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}hkcu.DeleteSubKey(keyname);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region "ISwAddin Implementation"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public bool ConnectToSW(object ThisSW, int Cookie)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp = (SldWorks)ThisSW;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}addinID = Cookie;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Setup callbacks
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.SetAddinCallbackInfo(0, this, addinID);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Setup the Command Manager
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iCmdMgr = iSwApp.GetCommandManager(Cookie);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AddCommandMgr();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Setup the Event Handlers
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SwEventPtr = iSwApp;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openDocs = new Hashtable();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Setup Sample Property Manager
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AddPMP();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public bool DisconnectFromSW()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RemoveCommandMgr();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RemovePMP();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DetachEventHandlers();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}GC.Collect();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region "UI Methods"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AddCommandMgr()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ICommandGroup cmdGroup = default(ICommandGroup);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BitmapHandler iBmp = new BitmapHandler();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Assembly thisAssembly = default(Assembly);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int cmdIndex0 = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int cmdIndex1 = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string Title = "C# Addin";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string ToolTip = "C# Addin";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int[] docTypes = { (int)swDocumentTypes_e.swDocASSEMBLY, (int)swDocumentTypes_e.swDocDRAWING, (int)swDocumentTypes_e.swDocPART };
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}thisAssembly = System.Reflection.Assembly.GetAssembly(this.GetType());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip, "", -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("test.ToolbarLarge.bmp", thisAssembly);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("test.ToolbarSmall.bmp", thisAssembly);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("test.MainIconLarge.bmp", thisAssembly);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("test.MainIconSmall.bmp", thisAssembly);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdIndex0 = cmdGroup.AddCommandItem2("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0, 1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdIndex1 = cmdGroup.AddCommandItem2("Show PMP", -1, "Display sample property manager", "Show PMP", 2, "ShowPMP", "PMPEnable", 2, 1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup.HasToolbar = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup.HasMenu = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}cmdGroup.Activate();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}foreach (int docType in docTypes)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}ICommandTab cmdTab = iCmdMgr.GetCommandTab(docType, Title);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}bool bResult = false;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (cmdTab == null)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cmdTab = iCmdMgr.AddCommandTab(docType, Title);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}CommandTabBox cmdBox = cmdTab.AddCommandTabBox();
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}int[] cmdIDs = new int[4];
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}int[] TextType = new int[4];
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cmdIDs[0] = cmdGroup.get_CommandID(cmdIndex0);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cmdIDs[1] = cmdGroup.get_CommandID(cmdIndex1);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}TextType[1] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cmdIDs[2] = cmdGroup.ToolbarId;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}TextType[2] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}bResult = cmdBox.AddCommands(cmdIDs, TextType);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}// Call GetCommands to confirm number of commands added
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}int buttonNumber = 0;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}object idObject = null;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}object textTypeObject = null;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}buttonNumber = cmdBox.GetCommands(out idObject, out textTypeObject);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Added " + buttonNumber + " commands.");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}CommandTabBox cmdBox1 = cmdTab.AddCommandTabBox();
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cmdIDs = new int[1];
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}TextType = new int[1];
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cmdIDs[0] = cmdGroup.ToolbarId;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}bResult = cmdBox1.AddCommands(cmdIDs, TextType);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}cmdTab.AddSeparator(cmdBox1, cmdGroup.ToolbarId);
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}thisAssembly = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iBmp.Dispose();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void RemoveCommandMgr()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iCmdMgr.RemoveCommandGroup(1);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public bool AddPMP()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ppage = new UserPMPage(this);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public bool RemovePMP()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ppage = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region "Event Methods"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Listen for events on all currently open docs
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventsToAllDocuments();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void DetachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DetachSWEvents();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Close events on all currently open docs
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DocumentEventHandler docHandler = default(DocumentEventHandler);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IDictionaryEnumerator _enumerator = openDocs.GetEnumerator();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}while (_enumerator.MoveNext())
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}docHandler = (DocumentEventHandler)_enumerator.Value;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}docHandler.DetachEventHandlers();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//This also removes the pair from the hash
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}docHandler = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//key = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.ActiveDocChangeNotify += this.SldWorks_ActiveDocChangeNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.DocumentLoadNotify2 += this.SldWorks_DocumentLoadNotify2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.FileNewNotify2 += this.SldWorks_FileNewNotify2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.ActiveModelDocChangeNotify += this.SldWorks_ActiveModelDocChangeNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.FileOpenPostNotify += this.SldWorks_FileOpenPostNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void DetachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.ActiveDocChangeNotify -= this.SldWorks_ActiveDocChangeNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.DocumentLoadNotify2 -= this.SldWorks_DocumentLoadNotify2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.FileNewNotify2 -= this.SldWorks_FileNewNotify2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.ActiveModelDocChangeNotify -= this.SldWorks_ActiveModelDocChangeNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp.FileOpenPostNotify -= this.SldWorks_FileOpenPostNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventsToAllDocuments()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 modDoc = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modDoc = (ModelDoc2)iSwApp.GetFirstDocument();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}while ((modDoc != null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (!openDocs.Contains(modDoc))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}AttachModelDocEventHandler(modDoc);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}modDoc = (ModelDoc2)modDoc.GetNext();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public bool AttachModelDocEventHandler(ModelDoc2 modDoc)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (modDoc == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DocumentEventHandler docHandler = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (!openDocs.Contains(modDoc))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}switch (modDoc.GetType())
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDocumentTypes_e.swDocPART:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}docHandler = new PartEventHandler(modDoc, this);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDocumentTypes_e.swDocASSEMBLY:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}docHandler = new AssemblyEventHandler(modDoc, this);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}case (int)swDocumentTypes_e.swDocDRAWING:
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}docHandler = new DrawingEventHandler(modDoc, this);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}docHandler.AttachEventHandlers();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}openDocs.Add(modDoc, docHandler);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void DetachModelEventHandler(ModelDoc2 modDoc)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openDocs.Remove(modDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modDoc = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region "Event Handlers"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int SldWorks_ActiveDocChangeNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//TODO: Add your implementation here
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int SldWorks_DocumentLoadNotify2(string docTitle, string docPath)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 modDoc = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modDoc = (ModelDoc2)iSwApp.GetFirstDocument();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}while ((modDoc != null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (modDoc.GetTitle() == docTitle)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (!openDocs.Contains(modDoc))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}AttachModelDocEventHandler(modDoc);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}modDoc = (ModelDoc2)modDoc.GetNext();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int SldWorks_FileNewNotify2(object newDoc, int doctype, string templateName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventsToAllDocuments();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int SldWorks_ActiveModelDocChangeNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//TODO: Add your implementation here
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int SldWorks_FileOpenPostNotify(string FileName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventsToAllDocuments();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region "UI Callbacks"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void CreateCube()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//make sure we have a part open
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string partTemplate = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 model = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FeatureManager featMan = default(FeatureManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}partTemplate = iSwApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}model = (ModelDoc2)iSwApp.NewDocument(partTemplate, (int)swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}model.InsertSketch2(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}model.SketchRectangle(0, 0, 0, 0.1, 0.1, 0.1, false);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Extrude the sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featMan = model.FeatureManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featMan.FeatureExtrusion(true, false, false, (int)swEndConditions_e.swEndCondBlind, (int)swEndConditions_e.swEndCondBlind, 0.1, 0.0, false, false, false,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}false, 0.0, 0.0, false, false, false, false, true, false, false
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}});
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void ShowPMP()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ppage.Show();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int PMPEnable()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int functionReturnValue = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (iSwApp.ActiveDoc == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = 1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return functionReturnValue;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
