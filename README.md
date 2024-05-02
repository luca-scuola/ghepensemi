# ghepensemi

La società GhePenseMi spa,  compagnia assicuratrice con sede a Milano in via della finanza 23, gestisce la propria clientela tramite una rete di filiali, una per ogni capoluogo di provincia.
GhePenseMi, con l'obbiettivo di fronteggiare meglio la concorrenza agguerrita delle compagnie online, decide di ristrutturare il ramo delle assicurazioni RC-Auto. 
Agli attuali 4 milioni di clienti sparsi su tutto il territorio nazionale sarà proposto un contratto che prevede un pagamento del premio di assicurazione proporzionale ai chilometri percorsi nel periodo annuale.
Per poter provvedere ai calcoli decide di installare un dispositivo in ogni veicolo assicurato.
Abbozzare un progetto, utilizzando le tecniche relative al protocollo MQTT ed alla gestione dei DB per le parti già conosciute e studiate, che consenta le seguenti operazioni:
•	ogni dispositivo installato su un’auto o su una moto trasmette la propria posizione ogni 3 secondi
•	in ogni filiale un server raccoglie i dati e calcola i chilometri percorsi
•	mensilmente ogni filiale invia un report al cliente indicando i chilometri percorsi

simulare il funzionamento degli eventuali sensori con flussi di dati in formato testo
