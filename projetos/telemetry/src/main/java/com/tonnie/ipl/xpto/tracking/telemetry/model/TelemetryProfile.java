package com.tonnie.ipl.xpto.tracking.telemetry.model;

import java.util.Set;
import java.util.UUID;

import javax.persistence.*;

import org.hibernate.annotations.GenericGenerator;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "telemetry_profiles")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class TelemetryProfile implements IEntity<UUID> {

	@Id
	@Column(name = "telemetry_profile_id")
	@GeneratedValue
	@GenericGenerator(name = "UUID", strategy = "org.hibernate.id.UUIDGenerator")
	private UUID id;

	@Column(name = "name")
	private String name;

	@ManyToMany(fetch = FetchType.EAGER)
	@JoinTable(name = "telemetry_profile_sensors", 
		joinColumns = @JoinColumn(name = "telemetry_profile_id"), 
		inverseJoinColumns = @JoinColumn(name = "sensors_id"))
	private Set<Sensor> sensors;

}
