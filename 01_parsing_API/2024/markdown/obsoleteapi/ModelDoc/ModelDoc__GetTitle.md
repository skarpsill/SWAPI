---
title: "ModelDoc::GetTitle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetTitle.htm"
---

# ModelDoc::GetTitle

This
method is obsolete and has been superseded by[ModelDoc2::GetTitle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetTitle.htm).

Description

This method retrieves the title of the document that appears in the
active window title bar.

Syntax (OLE Automation)

retval = ModelDoc.GetTitle ()

(Table)=========================================================

| Return: | (BSTR) retval | Title string, usually displayed on the window title bar |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetTitle ( &retval
)

(Table)=========================================================

| Output: | (BSTR) retval | Title string, usually displayed on the window title bar |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The document name that appears in the window header changes based on
your Microsoft Internet Explorer settings. If you chose to suppress known
file extensions, then the title shown in the window, and subsequently
returned by this method, will vary (for example, Part1.sldprt vs. Part1).

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetNames$$**$$ZGetInfoModelDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetTitle.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Close_Document_Example$$**$$Get_Model_Info_Example$$**$$ZExample_Get_Edit_In_Context$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetTitle.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
