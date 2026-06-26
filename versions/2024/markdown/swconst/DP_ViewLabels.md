---
title: "Document Properties > Views"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/DP_ViewLabels.htm"
---

# Document Properties > Views

HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"

(==============================================================)

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < Value > | Comments |
| --- | --- | --- | --- |
| Text - Font... | IModelDocExtension::GetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingViewTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified) IModelDocExtension::SetUserPreferenceTextFormat (swUserPreferenceTextFormat_e.swDetailingViewTextFormat,
swUserPreferenceOption_e.swDetailingNoOptionSpecified, < Value >) | See ITextFormat for font options | To set font property values, implement ITextFormat, set the appropriate
ITextFormat member values, and pass the ITextFormat object in the API
set method |
