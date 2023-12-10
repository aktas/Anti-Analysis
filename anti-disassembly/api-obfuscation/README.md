### API Obfuscation

`GetModuleHandleA` ve `GetProcAddress` işlevleri ile API çağrılarını doğrudan çağırmak yerine program çalışırken dinamik olarak çağırabiliriz. Bu sayede kullanacağımız API çağrılarının statik analizde tespit edilmemesini sağlamış oluruz. Ayrıca bu yöntemi `data obfuscation` ile biraz daha karmaşık hale getirebiliriz.
