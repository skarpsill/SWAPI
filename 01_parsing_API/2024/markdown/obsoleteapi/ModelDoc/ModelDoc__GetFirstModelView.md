---
title: "ModelDoc::GetFirstModelView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFirstModelView.htm"
---

# ModelDoc::GetFirstModelView

This
method is obsolete and has been superseded by[ModelDoc2::GetFirstModelView](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetFirstModelView.htm).

Description

This method gets the first view in a model document.

Syntax (OLE Automation)

retval = ModelDoc.GetFirstModelView
( )

(Table)=========================================================

| Return: | (LPDISPATCH)retval | Pointer to a Dispatch object, the first model view
in this document |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetFirstModelView
( &retval )

(Table)=========================================================

| Output: | (LPMODELVIEW) retval | Pointer to the first model view in this document |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful, S_FALSE if no model view is
being returned |

Remarks

You can traverse through the model views in a document
by using this method to get the initial view, and ModelView::GetNext to
get each of the following views. When ModelView::GetNext returns NULL,
you have reached the end of the list.

See also[ModelDoc::EnumModelViews](ModelDoc__EnumModelViews.htm)for a method for traversing the model views on a document.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ModelView_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetFirstModelView.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
