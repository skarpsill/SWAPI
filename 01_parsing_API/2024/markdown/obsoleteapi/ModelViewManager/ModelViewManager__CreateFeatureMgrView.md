---
title: "ModelViewManager::CreateFeatureMgrView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelViewManager/ModelViewManager__CreateFeatureMgrView.htm"
---

# ModelViewManager::CreateFeatureMgrView

This method is obsolete and has been superseded
by[ModelViewManager::CreateFeatureMgrView2](sldworksAPI.chm::/ModelViewManager/ModelViewManager__CreateFeatureMgrView2.htm).

Description

This method creates a new
tab on this FeatureManager design tree view.

Syntax (OLE Automation)

retval = ModelViewManager.CreateFeatureMgrView (
pPicture, toolTip, whichPane )

(Table)=========================================================

| Input: | (LPDISPATCH) pPicture | Pointer to the bitmap that you want to use for the tab |
| --- | --- | --- |
| Input: | (BSTR) toolTip | Text for the ToolTip |
| Input: | (long) whichPane | Pane to use as defined in swFeatMgrPane_e |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the new tab |

Syntax (COM)

status = ModelViewManager->CreateFeatureMgrView
( pPicture, toolTip, whichPane, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (LPDISPATCH) pPicture | Pointer to the bitmap that you want to use for the tab |
| --- | --- | --- |
| Input: | (BSTR) toolTip | Text for the ToolTip |
| Input: | (long) whichPane | Pane to use as defined in swFeatMgrPane_e |
| Output: | (LPFEATMGRVIEW) retval | Pointer to the new tab |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelViewManager\ModelViewManager__CreateFeatureMgrView.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="Items" value="ModelViewManager_Object$$**$$FeatMgrView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelViewManager\ModelViewManager__CreateFeatureMgrView.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
