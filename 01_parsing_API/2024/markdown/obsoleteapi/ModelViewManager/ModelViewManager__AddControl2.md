---
title: "ModelViewManager::AddControl2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelViewManager/ModelViewManager__AddControl2.htm"
---

# ModelViewManager::AddControl2

This method is obsolete and has been superseded
by[ModelViewManager::AddControl3](sldworksAPI.chm::/ModelViewManager/ModelViewManager__AddControl3.htm).

Description

This method adds an ActiveX
control to this model view.

NOTE:If your ActiveX control does not need tab traversal support, then use
ModelViewManager::AddControl.

Syntax (OLE Automation)

retval = ModelViewManager.AddControl2 ( Name, ControlName,
BstrLicKey )

(Table)=========================================================

| Input: | (BSTR) Name | User-defined label that appears on the tab |
| --- | --- | --- |
| Input: | (BSTR) ControlName | Name or class ID for the ActiveX control |
| Input: | (BSTR) BstrLicKey | Optional license key; this data is needed to create ActiveX controls
that require a runtime license key; if the ActiveX control supports licensing,
then provide a license key for the creation of the ActiveX control; default
value is NULL |
| Output: | (LPUNKNOWN) Retval | Pointer to the new ActiveX control |

Syntax (COM)

status = ModelViewManager->AddControl2 ( Name,
ControlName, BstrLicKey, &Retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) Name | User-defined label that appears on the tab |
| --- | --- | --- |
| Input: | (BSTR) ControlName | Name or class ID for the ActiveX control |
| Input: | (BSTR) BstrLicKey | Optional license key; this data only is needed to create ActiveX controls
that require a runtime license key; if the ActiveX control supports licensing,
then provide a license key for the creation of the ActiveX control; default
value is NULL |
| Output: | (LPUNKNOWN) Retval | Pointer to the new ActiveX control |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method sets the class
ID and license key information for the ActiveX control when the API PropertyManager
page is shown and the ActiveX control is created. The controlName argument
can be either the name of the control (ProgID) or the class ID (CLSID),
for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}".
Both provide the calendar protocol. You can obtain these strings using
a combination of the Microsoft OLE/COM Object Viewer and the registry
editor.

For example:

' ProgID

bRet = m_pActiveXControl.SetClass("MSCAL.Calendar",
"")

bRet = m_pActiveXControl2.SetClass("MSComctlLib.ListViewCtrl",
"")

' CLSID

bRet = m_pActiveXControl.SetClass("{8E27C92B-1264-101C-8A2F-040224009C02}",
"")

bRet = m_pActiveXControl2.SetClass("{BDD1F04B-858B-11D1-B16A-00C0F0283628}",
"")

To delete a tab created by this method, use
ModelViewManager::DeleteControlTab.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelViewManager\ModelViewManager__AddControl2.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelViewManager_Object$$**$$ModelViewManagerAddControl$$**$$ZGetModelViewMgrFeatMgrViews$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelViewManager\ModelViewManager__AddControl2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelViewManager_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelViewManager\ModelViewManager__AddControl2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
